from odoo import models, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains(
        'pricelist_id',
        'payment_term_id',
        'partner_id')
    def check_priority(self):
        if not self.user_has_groups('price_security.group_only_view'):
            return True

        # � Eliminada la validación de la pricelist
        # if (
        #         self.partner_id.property_product_pricelist and
        #         self.pricelist_id and
        #         self.partner_id.property_product_pricelist.sequence <
        #         self.pricelist_id.sequence):
        #     raise UserError(_(
        #         'Selected pricelist priority can not be higher than pricelist '
        #         'configured on partner'
        #     ))
        pass
