from odoo import api, models, tools
import logging
import os

_logger = logging.getLogger(__name__)

class ViewCompat(models.Model):
    _inherit = 'ir.ui.view'
    
    @api.model
    def _check_requires_list(self):
        """
        Detecta si el entorno actual requiere <list> o <tree> para las vistas de lista.
        """
        try:
            # Intenta crear una vista de prueba con <list>
            test_view = self.create({
                'name': 'test_list_view',
                'model': 'res.partner',
                'arch': '<list><field name="name"/></list>',
                'type': 'tree',
            })
            # Si llegamos aquí, <list> es aceptado
            test_view.unlink()
            return True
        except Exception:
            # Si hay un error, probablemente <list> no es aceptado
            return False
    
    @api.model
    def _fix_list_views(self):
        """
        Corrige las vistas de lista según el entorno.
        """
        requires_list = self._check_requires_list()
        _logger.info(f"Entorno detectado: {'<list>' if requires_list else '<tree>'} es requerido")
        
        tag_from = '<tree' if requires_list else '<list'
        tag_to = '<list' if requires_list else '<tree'
        end_tag_from = '</tree>' if requires_list else '</list>'
        end_tag_to = '</list>' if requires_list else '</tree>'
        
        # Buscar todas las vistas de tipo 'tree' del módulo
        views = self.search([
            ('model', 'like', 'mantenimientosq.'),
            ('type', '=', 'tree')
        ])
        
        for view in views:
            if view.arch and tag_from in view.arch:
                try:
                    new_arch = view.arch.replace(tag_from, tag_to).replace(end_tag_from, end_tag_to)
                    view.write({'arch': new_arch})
                    _logger.info(f"Vista corregida: {view.name} - {tag_from} -> {tag_to}")
                except Exception as e:
                    _logger.error(f"Error al corregir vista {view.name}: {e}")
  
    @api.model
    def create(self, vals):
        """
        Sobrescribe el método create para ajustar las vistas al crearlas.
        """
        if vals.get('type') == 'tree' and vals.get('arch') and 'mantenimientosq.' in vals.get('model', ''):
            requires_list = self._check_requires_list()
            if requires_list and '<tree' in vals['arch']:
                vals['arch'] = vals['arch'].replace('<tree', '<list').replace('</tree>', '</list>')
            elif not requires_list and '<list' in vals['arch']:
                vals['arch'] = vals['arch'].replace('<list', '<tree').replace('</list>', '</tree>')
        
        return super(ViewCompat, self).create(vals)
  
    def write(self, vals):
        """
        Sobrescribe el método write para ajustar las vistas al actualizarlas.
        """
        result = super(ViewCompat, self).write(vals)
        
        if vals.get('arch') and self.type == 'tree' and 'mantenimientosq.' in self.model:
            requires_list = self._check_requires_list()
            for view in self:
                if requires_list and '<tree' in view.arch:
                    new_arch = view.arch.replace('<tree', '<list').replace('</tree>', '</list>')
                    super(ViewCompat, view).write({'arch': new_arch})
                elif not requires_list and '<list' in view.arch:
                    new_arch = view.arch.replace('<list', '<tree').replace('</list>', '</tree>')
                    super(ViewCompat, view).write({'arch': new_arch})
        
        return result

