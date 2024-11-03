{
    'name': 'Serata Attendance',
    'version': '1.0',
    'summary': 'Manage Attendance',
    'description': 'A simple module for managing attendance.',
    'category': 'Productivity',
    'author': 'ahmad',
    'website': 'http://www.yourwebsite.com',
    'license': 'LGPL-3',
    'depends': ['base', 'hr'],
    'data': [
        'views/serata_attendance_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
