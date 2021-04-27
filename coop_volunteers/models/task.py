# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
   _name='coop.task'
   _description='Task Model'

   name = fields.Char(string='Task Name', required=True)
   description = fields.Text(string='Editor', required=False)
   start_time = fields.Date()
   

