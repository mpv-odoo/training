# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Ship(models.Model):
   _name='space.ship'
   _description='Space ship for space missions'

   model = fields.Char(string='Model', required=True)
   alias = fields.Char(string='Alias', required=True)
   capacity = fields.Integer()
   fuel = fields.Selection(string='Fuel Type', selection=[
      ('electric', 'Electric'),
      ('hydrogen', 'Hydrogen'),
      ('fusion', 'Fusion'),
      ('diesel', 'Diesel')
   ])
   size = fields.Selection(string='Size', selection=[
      ('small', 'Small'),
      ('medium', 'Medium'),
      ('large', 'Large')
      ], readonly=True)
   length = fields.Float(string="Ship Length in cm", required=False)
   width = fields.Float(string="Ship Width in cm", required=False)
   active = fields.Boolean(string='Active', default=True)


   @api.onchange('capacity')
   def _onchange_capacity(self):
      if self.capacity < 0:
         raise UserError('Capacity of a ship cannot be negative!')


   @api.constrains('length', 'width')
   def _recalc_size(self):
      for ship in self:
         if ship.length * ship.width < 85000:
            ship.size = 'small'
         elif ship.length * ship.width < 115000:
            ship.size = 'medium'
         else:
            ship.size = 'large'