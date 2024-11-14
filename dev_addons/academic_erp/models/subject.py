from odoo import models, fields

class Subject(models.Model):
    _name = 'academic_erp.subject'
    _description = 'Subject'

    name = fields.Char(string='Subject Name', required=True)
    course_ids = fields.Many2many('academic_erp.course', string='Courses')
    teacher_ids = fields.Many2many('academic_erp.teacher', string='Teachers')
