from odoo import fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    picking_note = fields.Html(
        string="Picking Note",
        help="This note will be visible on the delivery order.",
        translate=True,
    )
