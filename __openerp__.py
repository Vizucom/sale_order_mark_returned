# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2016- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Mark Sale Orders Returned',
    'category': 'Sale',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['sale'],
    'description': """
Mark Sale Orders Returned
=========================
 * Adds a new boolean field for marking sale orders as being Returned
 * Intended for situations where the SO has been confirmed and products shipped but later returned, and the SO should be flagged and hidden from list views

""",
    'data': [
        'views/sale_order.xml',
    ],

}
