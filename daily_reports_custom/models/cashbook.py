from odoo import api, models, _
from odoo.exceptions import UserError

class ReportCashBook(models.AbstractModel):
    _inherit = 'report.om_account_daily_reports.report_cashbook'

    @api.model
    def _get_report_values(self, docids, data=None):
        # === INICIO: Lógica de filtrado de sucursal y diarios ===

        # Sucursal principal del usuario
        user_store = self.env.user.store_id

        if not user_store:
            raise UserError(_("No tienes asignada una sucursal (store_id). Contacta a tu administrador."))

        # Sucursales hijas
        child_stores = self.env['res.store'].search([('parent_id', '=', user_store.id)])
        store_ids = [user_store.id] + child_stores.ids

        # Diarios permitidos (por todas las sucursales)
        stores = self.env['res.store'].browse(store_ids)
        journal_ids = []
        for store in stores:
            journal_ids += store.journal_ids.ids
        journal_ids = list(set(journal_ids))  # Unicos

        if not journal_ids:
            raise UserError(_("No hay diarios de caja configurados para tu sucursal ni hijas."))

        # Cuentas permitidas: todas las asociadas a movimientos de estos diarios
        allowed_account_ids = self.env['account.move.line'].search([
            ('journal_id', 'in', journal_ids)
        ]).mapped('account_id.id')
        allowed_account_ids = list(set(allowed_account_ids))

        # --- Filtrado de accounts según lo pedido en el wizard ---
        if not data.get('form') or not self.env.context.get('active_model'):
            raise UserError(_("Faltan datos para imprimir el reporte."))
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_ids', []))
        init_balance = data['form'].get('initial_balance', True)
        display_account = data['form'].get('display_account')
        sortby = data['form'].get('sortby', 'sort_date')
        codes = []

        # Filtrado de accounts:
        if data['form'].get('account_ids'):
            # El usuario pidió ciertas cuentas: sólo permitir las que pertenezcan a los diarios de la sucursal
            requested_account_ids = data['form']['account_ids']
            account_ids = list(set(requested_account_ids) & set(allowed_account_ids))
            if not account_ids:
                raise UserError(_("No tienes acceso a las cuentas seleccionadas."))
        else:
            # El usuario no seleccionó cuentas: usar todas las de los diarios permitidos
            account_ids = allowed_account_ids

        accounts = self.env['account.account'].search([('id', 'in', account_ids)])
        if not accounts:
            raise UserError(_("No se encontraron cuentas permitidas para mostrar en el reporte."))

        if data['form'].get('journal_ids', False):
            codes = [journal.code for journal in
                     self.env['account.journal'].search([
                         ('id', 'in', data['form']['journal_ids']),
                         ('id', 'in', journal_ids)
                     ])]
        else:
            codes = [journal.code for journal in self.env['account.journal'].browse(journal_ids)]

        # Aplica el contexto de comparación si lo hay (opcional)
        record = self.with_context(data['form'].get('comparison_context', {}))._get_account_move_entry(
            accounts, init_balance, sortby, display_account)
        return {
            'doc_ids': docids,
            'doc_model': model,
            'data': data['form'],
            'docs': docs,
            'time': __import__('time'),
            'Accounts': record,
            'print_journal': codes,
        }
