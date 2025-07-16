from odoo import models, fields

class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    internal_note = fields.Html(string="Internal Note",help="This note will be visible on the delivery order.",)