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
        'base',      
        'calendar',  
        'mail',      
        'website'    
    ],
    'data': [
        'security/academic_security.xml',
        'security/ir.model.access.csv',
        'views/notice_calendar_view.xml',
        'views/action_views.xml',
        'views/menu_views.xml',
        'views/course_views.xml',
        'views/student_views.xml',
        'views/parent_views.xml',
        'views/teacher_views.xml',
        'views/subject_views.xml',
        'views/notice_views.xml',
        'views/notice_recipient_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
