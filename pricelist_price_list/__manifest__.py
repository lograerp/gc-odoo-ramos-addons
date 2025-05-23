{
    'name': 'Pricelist Price List',
    'version': '16.0.1.0.0',
    'summary': 'Adds a view of every price for every product in the pricelist',
    'description': 'This module adds a view of every price for every product in the pricelist.',
    'author': 'Gauchocode',
    'license': 'GPL-3',
    'category': 'Warehouse',
    'depends': ['base', 'stock','tarif_restriction_by_user'],
    'data': [
        'views/pricelist_view.xml',
        'security/ir.model.access.csv',
        'security/product_pricelist_report_rules.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}