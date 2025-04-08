from odoo import api, fields, models, _

class MantenimientosQEquipmentCategory(models.Model):
    _name = 'mantenimientosq.equipment.category'
    _description = 'Categoría de Equipo'
    
    name = fields.Char('Nombre de Categoría', required=True)
    active = fields.Boolean(default=True)
    technician_user_id = fields.Many2one('res.users', string='Técnico')
    color = fields.Integer('Color Index')
    note = fields.Text('Notas')

