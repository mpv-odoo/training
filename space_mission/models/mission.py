# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Mission(models.Model):
   _name='space.mission'
   _description='Space Missions'

   name = fields.Char(string='Mission Name', required=True)
   description = fields.Text(string='Description')
   
   fuel_required = fields.Integer(string='Fuel Required')

   ship_id = fields.Many2one(comodel_name='space.ship',
                             string='Space Ship',
                             domain=('fuel_capacity', '>=', fuel_required)
   )
   captain_id = fields.Many2one(comodel_name='res.partner',
                                string='Crew Captain'
   )
   crew_ids = fields.Many2many(comodel_name='res.partner',
                               string='Crew Members'
   )


