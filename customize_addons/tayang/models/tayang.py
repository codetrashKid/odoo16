from odoo import fields, models

class TayangTaping(models.Model):
    _name = 'tayang.taping'
    _description = 'Master jadwal tayangan'

    name = fields.Char(string='Episode')
    dt_taping = fields.Date(string='Tanggal')
    version_id = fields.Many2one(comodel_name='tayang.version', string='Version')
    tema = fields.Char(string='Tema')

class TayangVersion(models.Model):
    _name = 'tayang.version'
    _description = 'Master data version'

    name = fields.Char(string='Version')
    status = fields.Selection(string='Status', selection=[('0', 'Inactive'), ('1', 'Active')])
    is_hide = fields.Boolean(string='Ditampilkan')



    