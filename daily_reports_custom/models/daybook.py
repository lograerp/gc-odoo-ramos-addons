from odoo import api, models, _
from odoo.exceptions import UserError
from datetime import timedelta, datetime

class ReportDayBook(models.AbstractModel):
    _inherit = 'report.om_account_daily_reports.report_daybook'

    @api.model
    def _get_report_values(self, docids, data=None):
        # Validación estándar
        if not data.get('form') or not self.env.context.get('active_model'):
            raise UserError(_("Form content is missing, this report cannot be printed."))

        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_ids', []))
        form_data = data['form']

        # === INICIO: Lógica de sucursal ===
        user_store = self.env.user.store_id
        if not user_store:
            raise UserError(_("No tienes asignada una sucursal (store_id). Contacta a tu administrador."))

        # Sucursales hijas
        child_stores = self.env['res.store'].search([('parent_id', '=', user_store.id)])
        store_ids = [user_store.id] + child_stores.ids

        # Diarios permitidos
        stores = self.env['res.store'].browse(store_ids)
        allowed_journal_ids = []
        for store in stores:
            allowed_journal_ids += store.journal_ids.ids
        allowed_journal_ids = list(set(allowed_journal_ids))

        if not allowed_journal_ids:
            raise UserError(_("No hay diarios configurados para tu sucursal ni hijas."))

        # Limitar los diarios a los permitidos
        if form_data.get('journal_ids'):
            # Filtra los diarios seleccionados contra los permitidos
            requested_journal_ids = form_data['journal_ids']
            journal_ids = list(set(requested_journal_ids) & set(allowed_journal_ids))
            if not journal_ids:
                raise UserError(_("No tienes acceso a los diarios seleccionados."))
        else:
            journal_ids = allowed_journal_ids

        # Limitar las cuentas a las relacionadas a esos diarios (en los movimientos)
        allowed_account_ids = self.env['account.move.line'].search([
            ('journal_id', 'in', journal_ids)
        ]).mapped('account_id.id')
        allowed_account_ids = list(set(allowed_account_ids))

        if not allowed_account_ids:
            raise UserError(_("No se encontraron cuentas permitidas para los diarios seleccionados."))

        accounts = self.env['account.account'].search([('id', 'in', allowed_account_ids)])

        # Fechas y lógica original
        date_from = datetime.strptime(form_data['date_from'], '%Y-%m-%d').date()
        date_to = datetime.strptime(form_data['date_to'], '%Y-%m-%d').date()
        codes = [journal.code for journal in self.env['account.journal'].browse(journal_ids)]
        dates = []
        record = []
        days_total = date_to - date_from
        for day in range(days_total.days + 1):
            dates.append(date_from + timedelta(days=day))
        for date in dates:
            date_data = str(date)
            # Hacemos override en form_data
            form_data['journal_ids'] = journal_ids
            accounts_res = self.with_context(form_data.get('comparison_context', {}))._get_account_move_entry(
                accounts, form_data, date_data)
            if accounts_res['lines']:
                record.append({
                    'date': date,
                    'debit': accounts_res['debit'],
                    'credit': accounts_res['credit'],
                    'balance': accounts_res['balance'],
                    'move_lines': accounts_res['lines']
                })
        return {
            'doc_ids': docids,
            'doc_model': model,
            'data': form_data,
            'docs': docs,
            'time': __import__('time'),
            'Accounts': record,
            'print_journal': codes,
        }
