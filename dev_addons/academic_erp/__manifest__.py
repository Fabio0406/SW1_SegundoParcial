{
    'name': 'Academic ERP',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage academic courses, students, parents, teachers, and subjects',
    'description': """
        This module provides an Academic ERP to manage courses of different levels and sections, along with students, parents, teachers, and subjects.
    """,
    'author': 'Dariana, Fabio y Lussiana',
    'depends': [
        'base',      # Módulo base obligatorio
        'calendar',  # Necesario para la vista de calendario
        'mail',      # Para notificaciones y mensajes
        'website'    # Opcional, para integrar con el portal web en caso de ser necesario
    ],
    'data': [
        'security/academic_security.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',         # Agregamos el archivo de menús
        'views/course_views.xml',
        'views/student_views.xml',
        'views/parent_views.xml',
        'views/teacher_views.xml',
        'views/subject_views.xml',
        'views/notice_views.xml',  # Vista de aviso
        'views/notice_calendar_view.xml',  # Vista de agenda
        'views/notice_recipient_view.xml', #vista destinatario
        'views/action_views.xml',       # Agregamos el archivo de acciones primero
        
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
