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
        'views/snippets/home.xml',
        'views/snippets/landing.xml'
        # 'views/snippets/home/banner.xml',
        # 'views/snippets/home/about_us.xml',
        # 'views/snippets/home/about_us2.xml',
        # 'views/snippets/home/accreditation.xml',
        # 'views/snippets/home/case_studies.xml',
        # 'views/snippets/home/designer_work.xml',
        # 'views/snippets/home/services.xml',
        # 'views/snippets/home/testimonal.xml',
        # 'views/snippets/home/follow_us.xml',
        # 'views/snippets/landing/about_banner.xml',
        # 'views/snippets/landing/about_cids.xml',
        # 'views/snippets/landing/cids_process.xml',
        # 'views/snippets/landing/hotel_services.xml',
        # 'views/snippets/landing/hotel_projects.xml',
        # 'views/snippets/landing/happy_customers.xml',
        # 'views/snippets/landing/why_us.xml'
    ],
    'images': [
    ],
    'assets':{
        'web.assets_frontend': [
            'cids_theme_odoo_15/static/src/scss/style.scss',
            'cids_theme_odoo_15/static/src/scss/landing_style.scss',
            'cids_theme_odoo_15/static/src/scss/owl.scss',
            'cids_theme_odoo_15/static/src/scss/owltheme.scss',
            'cids_theme_odoo_15/static/src/js/cids.js',
            'cids_theme_odoo_15/static/src/js/owl.js',
            'cids_theme_odoo_15/static/src/js/gallery.js',

        ],
    },
    'snippet_lists': {
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}