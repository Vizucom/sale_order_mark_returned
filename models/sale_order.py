# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _


class SaleOrder(osv.Model):

    _inherit = 'sale.order'

    _columns = {
        'returned': fields.boolean('Returned',
            help='''If the Sale Order's products have been shipped but then returned by the customer.''')
    }
