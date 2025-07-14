from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    price_list_1 = fields.Float("Lista Tarjeta 1/3 Pagos", compute="_compute_prices_pricelist_1_2", store=False)
    price_list_2 = fields.Float("Lista Efectivo", compute="_compute_prices_pricelist_1_2", store=False)

    @api.depends('list_price', 'product_variant_id')
    def _compute_prices_pricelist_1_2(self):
        for rec in self:
            price_1 = price_2 = 0.0
            if rec.product_variant_id:
                # Usar el recordset, no el id
                res = self.env['product.pricelist']._price_get(rec.product_variant_id, 1)
                price_1 = res.get(1, 0.0)
                price_2 = res.get(2, 0.0)
            rec.price_list_1 = price_1
            rec.price_list_2 = price_2
