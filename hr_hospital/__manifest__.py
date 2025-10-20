{
    "name": "Hr hospital",
    "version": "17.0.1.0.0",
    "category": "Human Resources",
    "license": "LGPL-3",
    "application": True,
    "installable": True,
    "assets": {
        "web.assets_backend": [
        ]
    },
    "data": [
        "security/ir.model.access.csv",

        "views/menu.xml",
        "views/hr_hospital_diseases_views.xml",
        "views/hr_hospital_doctor_views.xml",
        "views/hr_hospital_patient_views.xml",
        "views/hr_hospital_patient_visits_views.xml",

        "data/hr_hospital_diseases_data.xml",
    ],
    'demo': [
        'demo/hr_hospital_patient_demo.xml',
        'demo/hr_hospital_doctor_demo.xml',
    ],
    "depends": ["web", "hr"],
}
