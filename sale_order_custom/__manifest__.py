{
    'name': 'Sale Order Report Custom - Gauchocode',
    'version': '16.0.1.0.1',
    'summary': 'Sale Order Report Customizations for Gauchocode',
    'author': 'Gauchocode',
    'license': 'GPL-3',
    'category': 'Warehouse',
    'depends': ['base', 'sale', 'sale_order_report_format_custom'],
    'data': [
        'views/report_saleorder_price_unit_taxed.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}