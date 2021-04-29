# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Mission(models.Model):
   _name='space.mission'
   _description='Space Missions'

   name = fields.Char(
      string='Mission Name',
      required=True
   )
   description = fields.Text(
      string='Description'
   )
   fuel_required = fields.Integer(
      string='Fuel Required'
   )
   ship_id = fields.Many2one(
      comodel_name='space.ship',
      string='Mission Space Ship',
   )
   captain_id = fields.Many2one(
      comodel_name='res.partner',
      string='Crew Captain'
   )
   crew_ids = fields.Many2many(
      comodel_name='res.partner',
      string='Crew Members'
   )
   crew_size = fields.
   '''
      When fuel_required gets updated,
      update the domain rule for ship_id
      to only show ships that would be 
      able to make the trip
   '''
   @api.onchange('fuel_required')
   def filter_ships_by_fuel_cap(self):

      return {
         'domain': {
            'ship_id': [
               ('fuel_capacity', '>=', self.fuel_required)
            ]
         }
      }

