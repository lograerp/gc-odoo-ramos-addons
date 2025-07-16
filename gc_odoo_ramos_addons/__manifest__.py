{
    "name": "gc-odoo-ramos-addons",
    "version": "16.0.1.0.0",
    "category": "Tools",
    "summary": "Proyecto Ramos Revestimientos",
    "author": "Gauchocode",
    "license": "AGPL-3",
    'data': [
        "data/custom_permissions.xml",
        "security/ir.model.access.csv",
        "views/stock_views_custom.xml",
        "views/partner_views_custom.xml",
    ],
    "depends": ['base', 'sale_management', 'product'],
    "installable": True,
}