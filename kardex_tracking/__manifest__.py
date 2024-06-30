{
    'name': 'Product Kardex Wizard2',
    'version': '1.0',
    'summary': 'Wizard para visualizar movimientos de Kardex',
    'description': 'Este módulo permite visualizar los movimientos de Kardex de un producto en un rango de fechas.',
    'category': 'Inventory',
    'author': 'Tu Nombre',
    'website': '',
    'depends': ['stock', 'point_of_sale'],
    'data': [
        'views/product_kardex_wizard_views.xml',
        'views/menu_views.xml',
        'views/kardex_tracking_views.xml'
    ],
    'installable': True,
    'application': False,
}