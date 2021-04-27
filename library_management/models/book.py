# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
   _name='library.book'
   _description='Book Model'

   author = fields.Char(string='Author', required=True)
   editor = fields.Char(string='Editor', required=True)
   isbn = fields.Char(string='ISBN', required=False)
   year = fields.integer()
   genre = fields.Selection(string='Genre',
                              selection=[
                                 ('fantasy', 'Fantasy'),
                                 ('adventure', 'Adventure'),
                                 ('sci-fi', 'Science Fiction')
                              ],
                              copy=False
                           )

