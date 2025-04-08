{
'name': 'MantenimientosQ',
'version': '1.0',
'category': 'Maintenance',
'summary': 'Gestión de mantenimientos personalizados',
'description': """
    Módulo para gestionar mantenimientos personalizados con una interfaz similar
    al módulo de mantenimiento estándar de Odoo.
""",
'depends': ['base', 'mail', 'resource'],
'data': [
    'security/mantenimientosq_security.xml',
    'security/ir.model.access.csv',
    'views/mantenimientosq_views.xml',
    'views/mantenimientosq_team_views.xml',
    'views/mantenimientosq_equipment_views.xml',
    'views/mantenimientosq_config_views.xml',
    'views/mantenimientosq_report_views.xml',
    'views/mantenimientosq_menu.xml',
],
'demo': [],
'installable': True,
'application': True,
'auto_install': False,
'post_init_hook': 'post_init_hook',
}

