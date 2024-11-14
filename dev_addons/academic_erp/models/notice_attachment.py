from odoo import models, fields

class NoticeAttachment(models.Model):
    _name = 'academic_erp.notice.attachment'
    _description = 'Notice Attachment'

    name = fields.Char(string='Name', required=True)
    file = fields.Binary(string='File')
    file_type = fields.Selection([
        ('audio', 'Audio'),
        ('link', 'Link'),
        ('documento', 'Document'),
        ('video', 'Video')
    ], string='File Type', required=True)
    notice_id = fields.Many2one('academic_erp.notice', string='Notice', ondelete='cascade')