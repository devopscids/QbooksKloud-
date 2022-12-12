# -*- coding: utf-8 -*-

{
    'name': 'Theme Cids',
    'category': 'Theme/Corporate',
    'summary': """Theme Cids""",
    'version': '15.0.1.0',
    'depends': [
                'website','website_crm',
                'website_mass_mailing',
                ],
    'data': [
        'views/assets.xml',
        'views/footer_template.xml',
        # 'views/homepage.xml',

        # SNIPPETS
        'views/snippets/about_us.xml',
        'views/snippets/banner.xml',
        'views/snippets/banner2.xml',
        'views/snippets/clients.xml',
        'views/snippets/inspired.xml',
        'views/snippets/luxury_collection.xml',
        'views/snippets/our_services.xml',
        'views/snippets/recognition.xml',
        'views/snippets/testimonials.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'theme_cids/static/src/scss/common.scss',
            'theme_cids/static/src/scss/fonts.scss',
        ],
        'web._assets_primary_variables': [
            'theme_cids/static/src/scss/primary_variable.scss',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png',

    ],
    'application': False,
}
