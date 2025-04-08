from odoo import api, fields, models, _

class MantenimientosQActivityType(models.Model):
    _name = 'mantenimientosq.activity.type'
    _description = 'Tipo de Actividad de Mantenimiento'
    
    name = fields.Char('Nombre', required=True)
    active = fields.Boolean('Activo', default=True)
    description = fields.Text('Descripción')

