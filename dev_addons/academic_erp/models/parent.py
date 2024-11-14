from odoo import models, fields

class Parent(models.Model):
    _name = 'academic_erp.parent'
    _description = 'Parent'

    user_id = fields.Many2one('res.users', string='User', required=True, help='User associated with this parent')
    student_ids = fields.Many2many('academic_erp.student', string='Children')
    name = fields.Char(related='user_id.name', store=True, readonly=True, string="Parent Name")
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email', related='user_id.email', readonly=True)