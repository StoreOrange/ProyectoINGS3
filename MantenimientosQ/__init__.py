from . import models

def post_init_hook(cr, registry):
    """
    Ejecuta la corrección de vistas después de instalar el módulo   por Oded Garcia Ortiz.
    """
    from odoo import api, SUPERUSER_ID
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.ui.view']._fix_list_views()

#   A c t u a l i z a c i � n   p a r a   c o m p a t i b i l i d a d   t r e e / l i s t  
 