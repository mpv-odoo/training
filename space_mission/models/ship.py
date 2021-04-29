# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Ship(models.Model):
   _name='space.ship'
   _description='Space ship for space missions'

   model = fields.Char(
      string='Model',
      required=True                    
   )
   capacity = fields.Integer()
   fuel_type = fields.Selection(
      string='Fuel Type', 
      selection=[
         ('electric', 'Electric'),
         ('hydrogen', 'Hydrogen'),
         ('fusion', 'Fusion'),
         ('diesel', 'Diesel')]
   )
   max_range = fields.Float(
      string='Range in Astronomical Units',
      required=True
   )
   num_engines = fields.Integer(
      string='Number of Engines',
      default=1
   )
   length = fields.Float(
      string="Ship Length in meters",
      required=False
   )
   width = fields.Float(
      string="Ship Width in meters",
      required=False
   )
   size = fields.Text(
      string='Size', 
      compute='_recalc_size'
   )
   active = fields.Boolean(
      string='Active',
      default=True
   )

   @api.constrains('capacity')
   def _check_capacity(self):
      for ship in self:
         if ship.capacity < 0:
            raise UserError('Capacity of a ship cannot be negative!')

   @api.depends('length', 'width')
   def _recalc_size(self):
      for ship in self:
         if ship.length * ship.width < 85000:
            ship.size = 'Small'
         elif ship.length * ship.width < 115000:
            ship.size = 'Medium'
         else:
            ship.size = 'Large'


