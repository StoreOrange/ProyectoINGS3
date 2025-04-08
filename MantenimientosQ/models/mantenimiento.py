from odoo import models, fields, api

class MantenimientoEquipo(models.Model):
    _name = 'mantenimientosq.equipo'
    _description = 'Equipo para mantenimiento'

    name = fields.Char(string='Nombre', required=True)
    codigo = fields.Char(string='C?digo')
    descripcion = fields.Text(string='Descripci?n')
    fecha_adquisicion = fields.Date(string='Fecha de adquisici?n')
    estado = fields.Selection([
        ('operativo', 'Operativo'),
        ('mantenimiento', 'En mantenimiento'),
        ('inactivo', 'Inactivo'),
    ], string='Estado', default='operativo')
    
class MantenimientoSolicitud(models.Model):
    _name = 'mantenimientosq.solicitud'
    _description = 'Solicitud de mantenimiento'
    
    name = fields.Char(string='Referencia', required=True, copy=False, readonly=True, default='Nuevo')
    equipo_id = fields.Many2one('mantenimientosq.equipo', string='Equipo', required=True)
    fecha_solicitud = fields.Date(string='Fecha de solicitud', default=fields.Date.today)
    descripcion = fields.Text(string='Descripci?n del problema', required=True)
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('confirmado', 'Confirmado'),
        ('en_proceso', 'En proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ], string='Estado', default='borrador')
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('mantenimientosq.solicitud') or 'Nuevo'
        return super(MantenimientoSolicitud, self).create(vals)
		