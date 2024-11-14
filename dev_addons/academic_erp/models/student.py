from odoo import models, fields

class Student(models.Model):
    _name = 'academic_erp.student'
    _description = 'Student'

    user_id = fields.Many2one('res.users', string='User', required=True, help='User associated with this student')
    name = fields.Char(related='user_id.name', store=True, readonly=True, string="Student Name")
    age = fields.Integer(string='Age')
    course_id = fields.Many2one('academic_erp.course', string='Course')
    parent_ids = fields.Many2many('academic_erp.parent', string='Parents')
    email = fields.Char(related='user_id.email', readonly=True, string="Email")
