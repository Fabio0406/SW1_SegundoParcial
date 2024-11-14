from odoo import models, fields

class Course(models.Model):
    _name = 'academic_erp.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    level = fields.Selection([('primary', 'Primary'), ('secondary', 'Secondary')], string='Level', required=True)
    section = fields.Selection([('A', 'A'), ('B', 'B')], string='Section', required=True)
    student_ids = fields.One2many('academic_erp.student', 'course_id', string='Students')
    teacher_id = fields.Many2one('academic_erp.teacher', string='Teacher', help="Select the teacher assigned to this course")
    subject_ids = fields.Many2many('academic_erp.subject', string='Subjects')
