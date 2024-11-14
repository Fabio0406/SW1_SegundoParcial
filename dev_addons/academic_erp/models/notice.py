from odoo import models, fields, api

class Notice(models.Model):
    _name = 'academic_erp.notice'
    _description = 'Notice'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Agregar herencia para mensajes y actividades

    titulo = fields.Char(string='Title', required=True)
    descripcion = fields.Text(string='Description')
    tipo_especifico = fields.Selection([
        ('tarea', 'Task'),
        ('evento', 'Event'),
        ('examen', 'Exam'),
        ('comunicado', 'Announcement')
    ], string='Type', required=True)
    fecha_publicacion = fields.Datetime(string='Publication Date', default=fields.Datetime.now, required=True)
    destinatarios = fields.Selection([
        ('padres', 'Parents'),
        ('estudiantes', 'Students'),
        ('profesores', 'Teachers')
    ], string='Recipients', required=True)
    curso_id = fields.Many2one('academic_erp.course', string='Course')
    attachment_ids = fields.One2many('academic_erp.notice.attachment', 'notice_id', string='Attachments')
    recipients_ids = fields.One2many('academic_erp.notice.recipient', 'notice_id', string='Recipients Status')

    @api.model
    def create(self, vals):
        record = super(Notice, self).create(vals)
        user_domain = []

        if record.destinatarios == 'padres':
            user_domain = [('groups_id', 'in', self.env.ref('academic_erp.group_academic_parent').id)]
        elif record.destinatarios == 'estudiantes':
            user_domain = [('groups_id', 'in', self.env.ref('academic_erp.group_academic_student').id)]
        elif record.destinatarios == 'profesores':
            user_domain = [('groups_id', 'in', self.env.ref('academic_erp.group_academic_teacher').id)]
        
        if record.curso_id:
            if record.destinatarios == 'estudiantes':
                user_domain.append(('student_ids.course_id', '=', record.curso_id.id))
            elif record.destinatarios == 'profesores':
                user_domain.append(('teacher_ids.course_ids', '=', record.curso_id.id))

        users = self.env['res.users'].search(user_domain)

        # Crear registros de destinatarios y enviar notificaciones
        for user in users:
            recipient = self.env['academic_erp.notice.recipient'].create({
                'notice_id': record.id,
                'user_id': user.id,
                'state': 'recibido'
            })
            # Enviar notificación al usuario
            record.message_post(
                body=f"Tienes un nuevo aviso: {record.titulo}",
                partner_ids=[user.partner_id.id]
            )
        return record
    
    @api.model
    def get_user_notices_domain(self):
        current_user = self.env.user

        if current_user.has_group('base.group_system'):
            return []

        elif current_user.has_group('academic_erp.group_academic_parent'):
            child_ids = current_user.child_ids.mapped('id')
            return ['|', ('recipients_ids.user_id', '=', current_user.id), ('recipients_ids.user_id', 'in', child_ids)]

        else:
            return [('recipients_ids.user_id', '=', current_user.id)]

    @api.model
    def action_notice_calendar(self):
        action = self.env.ref('academic_erp.action_notice_calendar').read()[0]
        action['domain'] = self.get_user_notices_domain()
        return action