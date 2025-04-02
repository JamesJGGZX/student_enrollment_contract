# -*- coding: utf-8 -*-
{
    "name": "Student Enrollment Contract",
    "version": "1.6.0",
    "summary": "Manage student enrollment contracts with subjects and payments",
    "sequence": -1,
    "description": """
Student Enrollment Contract
===========================

This module allows educational institutions to manage student contracts,
including selected subjects, assigned teachers, total cost, and payment tracking.
    """,
    "author": "Isaac Blanco",
    "company": "MicaGroup",
    # "website": "",
    "contributors": [
        "Isaac Blanco - <jamesblancozx@gmail.com>"
    ],
    "category": "Education",
    "depends": ["base","contacts", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_students_contract_data.xml",
        "data/ir_sequence_students_contract_payment_data.xml",
        "wizard/add_contract_payment_views.xml",
        "views/students_contract_views.xml",
        "views/enrollment_subject_views.xml",
        "views/res_partner_inherit_views.xml",
        "views/product_template_inherit_views.xml",
        "views/menus.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "student_enrollment_contract/static/src/components/**/*.js",
            "student_enrollment_contract/static/src/components/**/*.xml",
            "student_enrollment_contract/static/src/components/**/*.scss",
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}