from odoo import models, fields, api
from datetime import datetime

class ProductPricelistReport(models.Model):
    _name = 'product.pricelist.report'
    _description = 'Reporte de Precios por Tarifa'

    product_id = fields.Many2one('product.product', string='Producto', readonly=True)
    pricelist_id = fields.Many2one('product.pricelist', string='Tarifa', readonly=True)
    price = fields.Float(string='Precio', readonly=True)

    # Solo uno, para guardar info del reporte
    last_generated = fields.Datetime(string='Última generación', readonly=True)

    @api.model
    def generate_data(self):
        """Genera los registros de precios por producto y tarifa"""
        self.search([]).unlink()

        products = self.env['product.product'].search([])
        pricelists = self.env['product.pricelist'].search([])

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

        # Guardamos una línea especial como "marca" con la fecha de generación
        self.env['product.pricelist.report'].create({
            'product_id': None,
            'pricelist_id': None,
            'price': 0.0,
            'last_generated': datetime.now()
        })

    @api.model
    def open_or_generate_report(self):
        """Si no hay datos, genera el reporte. Si hay, solo abre la vista."""
        if not self.search([], limit=1):
            self.generate_data()

        return self.env.ref('pricelist_price_list.action_product_pricelist_report_window').read()[0]

