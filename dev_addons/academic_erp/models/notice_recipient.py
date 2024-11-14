from odoo import models, fields, api

class NoticeRecipient(models.Model):
    _name = 'academic_erp.notice.recipient'
    _description = 'Notice Recipient'

    notice_id = fields.Many2one('academic_erp.notice', string='Notice', required=True, ondelete='cascade')
    user_id = fields.Many2one('res.users', string='User', required=True)
    state = fields.Selection([
        ('no_recibido', 'Not Received'),
        ('recibido', 'Received'),
        ('no_leido', 'Not Read'),
        ('leido', 'Read')
    ], string='Status', default='recibido', required=True)

    # Campos relacionados para mostrar detalles del aviso
    notice_title = fields.Char(related='notice_id.titulo', string='Notice Title', readonly=True)
    notice_type = fields.Selection(related='notice_id.tipo_especifico', string='Type', readonly=True)
    notice_publication_date = fields.Datetime(related='notice_id.fecha_publicacion', string='Publication Date', readonly=True)

    def mark_as_read(self):
        for record in self:
            if record.state in ['recibido']:
                record.state = 'leido'  # Cambia el estado a 'leido'