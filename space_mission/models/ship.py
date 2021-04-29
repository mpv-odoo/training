# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Ship(models.Model):
   _name='space.ship'
   _description='Space ship for space missions'

   model = fields.Char(string='Model',
                       required=True                    
   )
   alias = fields.Char(string='Alias',
                       required=True
   )
   capacity = fields.Integer()
   
   fuel_type = fields.Selection(string='Fuel Type', 
                                selection=[
                                 ('electric', 'Electric'),
                                 ('hydrogen', 'Hydrogen'),
                                 ('fusion', 'Fusion'),
                                 ('diesel', 'Diesel')],
   )
   fuel_capacity = fields.Float(string='Fuel Tank Capacity in Liters', required=True)
   num_engines = fields.Integer(string='Number of Engines', default=1)


   size = fields.Selection(string='Size', selection=[
      ('small', 'Small'),
      ('medium', 'Medium'),
      ('large', 'Large')
      ], readonly=True)
   length = fields.Float(string="Ship Length in cm", required=False)
   width = fields.Float(string="Ship Width in cm", required=False)
   active = fields.Boolean(string='Active', default=True)


   @api.constrains('capacity')
   def _check_capacity(self):
      for ship in self:
         if ship.capacity < 0:
            raise UserError('Capacity of a ship cannot be negative!')


   @api.onchange('length', 'width')
   def _recalc_size(self):
         if self.length * self.width < 85000:
            self.size = 'small'
         elif self.length * self.width < 115000:
            self.size = 'medium'
         else:
            self.size = 'large'