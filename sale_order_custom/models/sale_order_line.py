from odoo import models, api, exceptions, _
from odoo.tools.float_utils import float_is_zero

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _check_price_unit_permission(self, vals):
        """Restricción: sólo los managers pueden cambiar el precio unitario."""
        if 'price_unit' not in vals:
            return

        # Saltar validación si usuario es gerente de ventas
        if self.env.user.has_group('sales_team.group_sale_manager'):
            return

        for line in self:
            product = line.product_id
            pricelist = line.order_id.pricelist_id

            # Obtener el precio de lista
            product_price = pricelist._get_product_price(
            product,
            quantity=1.0,
            uom=line.product_uom,
            date=line.order_id.date_order
        )


            if not float_is_zero(vals['price_unit'] - product_price, precision_digits=2):
                raise exceptions.UserError(_(
                    "No tenés permisos para modificar el precio unitario del producto. "
                    "Debe coincidir con el precio de lista."
                ))

    def write(self, vals):
        self._check_price_unit_permission(vals)
        return super().write(vals)

    @api.model
    def create(self, vals):
        record = super().create(vals)
        record._check_price_unit_permission(vals)
        return record
