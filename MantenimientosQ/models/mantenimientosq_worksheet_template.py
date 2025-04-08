from odoo import api, fields, models, _

class MantenimientosQWorksheetTemplate(models.Model):
    _name = 'mantenimientosq.worksheet.template'
    _description = 'Plantilla de Hoja de Trabajo'
    
    name = fields.Char('Nombre', required=True)
    active = fields.Boolean('Activo', default=True)
    description = fields.Text('Descripción')
    instruction = fields.Html('Instrucciones')

