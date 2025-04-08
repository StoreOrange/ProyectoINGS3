from odoo import api, fields, models, _

class MantenimientosQStage(models.Model):
    _name = 'mantenimientosq.stage'
    _description = 'Etapa de Mantenimiento'
    _order = 'sequence, id'
    
    name = fields.Char('Nombre', required=True, translate=True)
    sequence = fields.Integer('Secuencia', default=10)
    fold = fields.Boolean('Plegado en Kanban')
    active = fields.Boolean('Activo', default=True)
    description = fields.Text('Descripción')

