{
    'name': "Estimation For Job",
    'version': '16.0.1.0.0',
    'summary': """Estimation for Jobs""",
    'description': 'Estimation for Jobs',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/job_estimation.xml',
        'views/job_type.xml',
        'views/menu.xml',

    ],
    # 'license': 'AGPL-3',
    'installable': True,
    'application': False,
}
