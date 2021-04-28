# -*- coding: utf-8 -*-
{
   'name': 'Library Management',
   'summary': """A module to keep track of all books in the library""",
   'description': """
      The library module keeps track of:
      - Authors
      - Editors
      - Publisher
      - year of edition
      - ISBN
      - Genre
   """,
   'author': 'Odoo',
   'website': 'https://www.odoo.com',
   'category': 'Training',
   'version': '0.1',
   'depends': ['base'],
   'data': [
      'security/library_security.xml',
      'security/ir.model.access.csv'
   ],
   'demo': [
   ],
}