# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ship(models.Model):
   _name='space.ship'
   _description='Space ship for space missions'

   model = fields.Char(string='Model', required=True)
   capacity = fields.Integer()
   active = fields.Boolean(string='Active', default=True)