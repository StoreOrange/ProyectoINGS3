from odoo import api, fields, models, _

class MantenimientosQEquipment(models.Model):
    _name = 'mantenimientosq.equipment'
    _description = 'Equipo de Mantenimiento Q'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Nombre del Equipo', required=True, tracking=True)
    active = fields.Boolean(default=True)
    team_id = fields.Many2one('mantenimientosq.team', string='Equipo de Mantenimiento')
    serial_no = fields.Char('Número de Serie', tracking=True)
    model = fields.Char('Modelo')
    category_id = fields.Many2one('mantenimientosq.equipment.category', string='Categoría')
    assign_date = fields.Date('Fecha de Asignación')
    effective_date = fields.Date('Fecha Efectiva')
    technician_user_id = fields.Many2one('res.users', string='Técnico')
    maintenance_count = fields.Integer(compute='_compute_maintenance_count', string="Mantenimientos")
    maintenance_ids = fields.One2many('mantenimientosq.request', 'equipment_id', string='Mantenimientos')
    note = fields.Text('Notas')
    
    def _compute_maintenance_count(self):
        for equipment in self:
            equipment.maintenance_count = self.env['mantenimientosq.request'].search_count([
                ('equipment_id', '=', equipment.id)
            ])

