# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
   _inherit = 'project'

   test = fields.Char(
      string='Testing'
   )