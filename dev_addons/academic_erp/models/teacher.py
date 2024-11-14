from odoo import models, fields, api

class Teacher(models.Model):
    _name = 'academic_erp.teacher'
    _description = 'Teacher'

    user_id = fields.Many2one('res.users', string='User', required=True, help='User associated with this teacher')
    subject_ids = fields.Many2many('academic_erp.subject', string='Subjects')
    course_ids = fields.One2many('academic_erp.course', 'teacher_id', string='Courses')
    name = fields.Char(related='user_id.name', store=True, readonly=True, string="Teacher Name")
