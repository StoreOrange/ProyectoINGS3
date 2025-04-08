from odoo import api, fields, models, _

class MantenimientosQTeam(models.Model):
    _name = 'mantenimientosq.team'
    _description = 'Equipo de Mantenimiento Q'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Nombre del Equipo', required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer('Color Index')
    todo_count = fields.Integer(string="Número de tareas por hacer", compute='_compute_todo_count')
    
    def _compute_todo_count(self):
        for team in self:
            team.todo_count = self.env['mantenimientosq.request'].search_count([
                ('team_id', '=', team.id),
                ('state', '=', 'new')
            ])

