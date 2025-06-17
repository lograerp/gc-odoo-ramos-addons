from odoo import models, fields, api

class Product(models.Model):
    _inherit = 'product.product'

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        product_ids = records.ids

        def after_commit():
            self.env['product.pricelist.report'].update_prices_for_products(product_ids)

        self.env.cr.postcommit.add(after_commit)
        return records

    def write(self, vals):
        res = super().write(vals)
        product_ids = self.ids

        def after_commit():
            self.env['product.pricelist.report'].update_prices_for_products(product_ids)

        self.env.cr.postcommit.add(after_commit)
        return res

