{
    'name': 'CIDS DESIGN Theme',
    'description': 'CIDS HOME PAGE',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website','web'],
    'data': [
        'views/assets.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/snippets/banner.xml',
        'views/snippets/about_us.xml',
        'views/snippets/about_us2.xml',
        'views/snippets/accreditation.xml',
        'views/snippets/case_studies.xml',
        'views/snippets/designer_work.xml',
        'views/snippets/services.xml',
        'views/snippets/testimonal.xml',
        'views/snippets/follow_us.xml'
    ],
    'images': [
    ],
    'assets':{
        'web.assets_frontend': [
            'cids_theme_odoo_15/static/src/scss/style.scss',
            'cids_theme_odoo_15/static/src/scss/owl.scss',
            'cids_theme_odoo_15/static/src/scss/owltheme.scss',
            'cids_theme_odoo_15/static/src/js/cids.js',
            'cids_theme_odoo_15/static/src/js/owl.js',

        ],
    },
    'snippet_lists': {
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
