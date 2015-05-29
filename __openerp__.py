# -*- coding: utf-8 -*-
{
    'name': "attendance",

    'summary': """
        A small module to fix the attendance module of OpenEduCat""",

    'description': """
        This is a fix for issue #19 https://github.com/openeducat/openeducat_erp/issues/19
        in OpenEduCat. Since the original repository is using deprecated code, this code
        should belong to a separate repo till there are no plans of upgrading the original repo.
    """,

    'author': "Aman Gautam",
    'website': "http://github.com/aman-gautam",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['openeducat_erp'],

    # always loaded
    'data': [
        'view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}