from odoo import fields, models, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_note = fields.Html(
        string="Sale Order Note",
        help="This note comes from the related sale order.",
        related='sale_id.picking_note',
        readonly=True,
        store=True,
        translate=True,
    )
