{
    'name': 'Project Management',
    'version': '15.0.0.1.0',
    'summary': 'Manage Projects and Tasks',
    'description': """
Custom Project and Task Management
==================================
- Create and manage projects and tasks.
- Restrict project creation/editing to Project Managers.
- View permissions for all authenticated users.
""",
    'author': 'Jothimani Rajagopal / MarsDevs',
    'website': 'https://marsdevs.com',
    'category': 'Project',
    'depends': ['base', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/task_views.xml',
        'views/project_task_stage_views.xml',
        'views/menu.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
