# -*- coding: utf-8 -*-

from odoo import models, fields, api

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



   active = fields.Boolean(string='Active', default=True)