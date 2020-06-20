# -*- coding: utf-8 -*-
{
    'name': "surgi_ess",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_attendance','hr_holidays'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/employee_directory.xml',
        'views/attendance.xml',
        'views/employee_profile.xml',
        'views/leaves.xml',
        'views/allocate_leave.xml',
        'views/my_permissions.xml',
        'views/missions.xml',
        'views/hr_leave_type.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
