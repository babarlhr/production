# -*- coding: utf-8 -*-
{
    'name': "Surgi-Tech Attendance Sheet Customizations",
    'summary': """
    """,
    'description': """
    """,
    'author': "Ramadan Khalil",
    'website': "https://www.linkedin.com/in/ramadan-khalil-a7088164/",
    'version': '0.1',
    'depends': ['base', 'rm_hr_attendance_sheet', 'planning'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hr_contract_view.xml',
        'views/hr_attendance_policy_view.xml',
        'views/hr_attendance_sheet_view.xml',
        'views/hr_attendance_penalty_view.xml'
    ],
}
