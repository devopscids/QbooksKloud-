
from odoo.http import request
from odoo import http

class DemoClass(http.Controller):

    @http.route(['/landing_test'], type='http', auth="public", website=True)
    def landing_page(self, **post):
        return request.render("cids_theme_odoo_15.landing_page")

    @http.route(['/commercial_test'], type='http', auth="public", website=True)
    def commercial_page(self, **post):
        return request.render("cids_theme_odoo_15.commercial")

    @http.route(['/hospitality_test'], type='http', auth="public", website=True)
    def hospitality_page(self, **post):
        return request.render("cids_theme_odoo_15.hospitality")
