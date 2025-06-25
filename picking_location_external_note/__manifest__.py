{
    'name': 'Picking location External Note',
    'version': '16.0.1.0.1',
    'summary': 'Adds the location.external_note field to the picking report',
    'author': 'Gauchocode',
    'license': 'GPL-3',
    'category': 'Warehouse',
    'depends': ['base', 'stock'],
    'data': [
        'views/stock_picking_report_views.xml',
        'views/report_custom_ramos_header.xml',
        'views/stock_picking_custom.xml',
        'views/hide_stock_report.xml',

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}