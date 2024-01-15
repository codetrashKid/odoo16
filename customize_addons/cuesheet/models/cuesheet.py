from odoo import fields, models

class CuesheetTaping(models.Model):
    _name = 'cuesheet.taping'
    _description = 'Master Episode'

    name = fields.Char(string='Episode')
    dt_taping = fields.Date(string='Tanggal')
    version_id = fields.Many2one(comodel_name='cuesheet.tapingversion', string='Version')
    tema = fields.Char(string='Tema')
    dt_program = fields.Date(string='Tanggal Program')
    catatan = fields.Char(string='Catatan')
    rating = fields.Integer(string='Rating')


class CuesheetTapingVersion(models.Model):
    _name = 'cuesheet.tapingversion'
    _description = 'Master versi episode'

    name = fields.Char(string='Version')
    status = fields.Selection(string='Status', selection=[('0', 'Inactive'), ('1', 'Active')])
    is_hide = fields.Boolean(string='Ditampilkan')


class Product(models.Model):
    _inherit = 'product.product'

    sisgesit_product_id = fields.Integer(string='ID sisgesit')

    