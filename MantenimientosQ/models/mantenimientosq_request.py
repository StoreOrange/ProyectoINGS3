from odoo import api, fields, models, _

class MantenimientosQRequest(models.Model):
    _name = 'mantenimientosq.request'
    _description = 'Solicitud de Mantenimiento Q'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
    team_id = fields.Many2one('mantenimientosq.team', string='Equipo', required=True)
    equipment_id = fields.Many2one('mantenimientosq.equipment', string='Equipo')
    user_id = fields.Many2one('res.users', string='Responsable')
    state = fields.Selection([
        ('new', 'Por hacer'),
        ('in_progress', 'En progreso'),
        ('done', 'Completado'),
        ('canceled', 'Cancelado')
    ], string='Estado', default='new', tracking=True)
    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Normal'),
        ('2', 'Alta'),
        ('3', 'Muy Alta')
    ], string='Prioridad', default='1')
    date_request = fields.Date('Fecha de solicitud', default=fields.Date.today)
    date_scheduled = fields.Date('Fecha programada')
    date_completed = fields.Date('Fecha de finalización')

