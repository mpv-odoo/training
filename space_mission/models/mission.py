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
   travel_distance = fields.Integer(
      string='Distance to be traveled in the mission'
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
      string='Crew Members',
      comodel_name='res.partner'
   )
   crew_size = fields.Integer(
      string='Crew Size',
      compute='_calc_crew_size'
   )
   '''
      When travel_distance gets updated,
      update the domain rule for ship_id
      to only show ships that would be 
      able to make the trip
   '''
   @api.onchange('fuel_required')
   def filter_ships_by_range(self):
      for rec in self:
         return {
            'domain': {
               'ship_id': [
                  ('max_range', '>=', rec.distance_travelled)
               ]
            }
         }

   @api.depends('crew_ids')
   def _calc_crew_size(self):
      for mission in self:
         mission.crew_size = len(mission.crew_ids)