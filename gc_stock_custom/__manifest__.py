{
    'name': 'Gauchocode Stock Custom',
    'version': '16.0.1.0.1',
    'summary': 'Customizations for Stock for Ramos',
    'author': 'Gauchocode',
    'license': 'GPL-3',
    'category': 'Warehouse',
    'depends': ['base', 'stock','sale','sale_stock'],
    'data': [
        'views/stock_picking_report_views.xml',
        'views/report_custom_ramos_header.xml',
        'views/stock_picking_custom.xml',
        'views/hide_stock_report.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_type_custom.xml',

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}