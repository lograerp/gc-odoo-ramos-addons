from odoo import models, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):
        report_sudo = self._get_report(report_ref)
        model = report_sudo.model

        _logger.info("Rendering PDF for report: %s, model: %s, res_ids: %s", report_ref, model, res_ids)

        if model == 'account.move' and res_ids:
            if isinstance(res_ids, int):
                res_ids = [res_ids]
            if isinstance(res_ids, (list, tuple)) and all(isinstance(r, int) for r in res_ids):
                records = self.env[model].browse(res_ids)
                for rec in records:
                    _logger.info("Checking journal restriction for move: %s (journal: %s)", rec.name, rec.journal_id.name)
                    if getattr(rec.journal_id, "restrict_invoice_print", False):
                        raise UserError(_("No está permitido imprimir facturas de este diario."))

        return super()._render_qweb_pdf(report_ref, res_ids=res_ids, data=data)
