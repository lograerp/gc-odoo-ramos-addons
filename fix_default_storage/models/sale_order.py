from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('user_id', 'company_id')
    def _compute_warehouse_id(self):
        IrDefault = self.env['ir.default']

        for order in self:
            user = order.user_id.with_company(order.company_id.id)

            if order.state in ['draft', 'sent'] or not order.ids:
                if user.property_warehouse_id:
                    order.warehouse_id = user.property_warehouse_id
                elif user.store_ids:
                    order.warehouse_id = user.store_ids[0].warehouse_ids[0]
                else:
                    default_warehouse_id = IrDefault.with_company(order.company_id.id)\
                                                    .get_model_defaults('sale.order').get('warehouse_id')
                    order.warehouse_id = default_warehouse_id or False
