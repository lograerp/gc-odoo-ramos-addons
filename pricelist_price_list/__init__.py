from . import models

from odoo import api, SUPERUSER_ID

def post_init_generate_pricelist_report(cr, registry):
    """Hook post instalación: generar todos los registros del reporte de precios"""
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['product.pricelist.report'].generate_data(batch_size=100)
