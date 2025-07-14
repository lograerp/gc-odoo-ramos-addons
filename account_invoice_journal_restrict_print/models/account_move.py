# -*- coding: utf-8 -*-
from odoo import models, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_print_invoice(self):
        for move in self:
            if move.journal_id.restrict_invoice_print:
                raise UserError(_('No está permitido imprimir facturas de este diario.'))
        return super().action_print_invoice()
