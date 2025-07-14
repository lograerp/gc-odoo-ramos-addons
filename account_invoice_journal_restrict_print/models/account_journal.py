# -*- coding: utf-8 -*-
from odoo import models, fields

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    restrict_invoice_print = fields.Boolean(
        string='Restringir impresión de factura',
        help='Si está activo, no se podrán imprimir facturas de este diario.'
    )
