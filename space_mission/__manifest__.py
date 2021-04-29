# -*- coding: utf-8 -*-
{
    'name': 'Space Mission',
    'summary': """Academy app to manage training""",
    'description': """
         Space Ship module to keep track of all 
         current space ships
      """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/space_security.xml',
        'security/ir.model.access.csv',
        'views/space_menuitems.xml',
        'views/ship_views.xml',
        'views/mission_views.xml'
    ],
    'demo': [
       'demo/ships_demo.xml'
    ],
}