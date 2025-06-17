import logging
import threading
from odoo import models, fields, api
from datetime import datetime
from odoo import registry



_logger = logging.getLogger(__name__)

class ProductPricelistReport(models.Model):
    _name = 'product.pricelist.report'
    _description = 'Reporte de Precios por Tarifa'

    product_id = fields.Many2one('product.product', string='Producto', readonly=True)
    pricelist_id = fields.Many2one('product.pricelist', string='Tarifa', readonly=True)
    price = fields.Float(string='Precio', readonly=True)
    last_generated = fields.Datetime(string='Última generación', readonly=True)

    @api.model
    def update_prices_for_products(self, product_ids):
        """Lanza un thread para actualizar precios de productos específicos"""
        db_name = self.env.cr.dbname
        user_id = self.env.uid  # ✅ lo obtenemos afuera del thread

        def run():
            with registry(db_name).cursor() as cr:
                env = api.Environment(cr, user_id, {})
                report_model = env['product.pricelist.report']
                product_model = env['product.product']
                pricelist_model = env['product.pricelist']

                products = product_model.browse(product_ids)
                pricelists = pricelist_model.search([])

                records = []
                for product in products:
                    for pricelist in pricelists:
                        price_dict = pricelist._get_products_price(products=product, quantity=1.0)
                        price = price_dict.get(product.id, 0.0)

                        existing = report_model.search([
                            ('product_id', '=', product.id),
                            ('pricelist_id', '=', pricelist.id)
                        ], limit=1)

                        if existing:
                            existing.write({
                                'price': price,
                                'last_generated': datetime.now()
                            })
                        else:
                            records.append({
                                'product_id': product.id,
                                'pricelist_id': pricelist.id,
                                'price': price,
                                'last_generated': datetime.now()
                            })

                if records:
                    report_model.create(records)

                cr.commit()
                _logger.info("Actualización de precios terminada para productos %s", product_ids)

        threading.Thread(target=run, name="UpdatePricelistReport").start()

    @api.model
    def generate_data(self, batch_size=100):
        """Genera los registros de precios por producto y tarifa, en lotes."""
        _logger.info("Iniciando generación del reporte de precios por tarifa...")
        self.search([]).unlink()

        Product = self.env['product.product']
        Pricelist = self.env['product.pricelist']
        pricelists = Pricelist.search([])
        total = Product.search_count([])

        offset = 0
        processed = 0
        while True:
            products = Product.search([], offset=offset, limit=batch_size)
            if not products:
                break

            records = []
            for product in products:
                for pricelist in pricelists:
                    price_dict = pricelist._get_products_price(products=product, quantity=1.0)
                    price = price_dict.get(product.id, 0.0)
                    records.append({
                        'product_id': product.id,
                        'pricelist_id': pricelist.id,
                        'price': price,
                        'last_generated': datetime.now()
                    })

            self.create(records)
            processed += len(products)
            offset += batch_size
            _logger.info("Procesados %s de %s productos...", processed, total)

        # Línea especial como "marca" de generación
        self.create({
            'product_id': None,
            'pricelist_id': None,
            'price': 0.0,
            'last_generated': datetime.now()
        })

        _logger.info("Generación completada. Se procesaron %s productos.", total)


    @api.model
    def open_or_generate_report(self):
        """Si no hay datos, genera el reporte. Si hay, solo abre la vista."""
        #if not self.search([], limit=1):
        #    self.generate_data()

        return self.env.ref('pricelist_price_list.action_product_pricelist_report_window').read()[0]

