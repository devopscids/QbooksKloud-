from odoo.http import request
from odoo import http


class DemoClass(http.Controller):

    @http.route(['/'], type='http', auth="public", website=True)
    def home_page(self, **post):
        return request.render("cids_theme_odoo_15.home")

    @http.route(['/landing'], type='http', auth="public", website=True)
    def landing_page(self, **post):
        return request.render("cids_theme_odoo_15.landing_page")

    @http.route(['/commercial'], type='http', auth="public", website=True)
    def commercial_page(self, **post):
        return request.render("cids_theme_odoo_15.commercial")

    @http.route(['/hospitality'], type='http', auth="public", website=True)
    def hospitality_page(self, **post):
        return request.render("cids_theme_odoo_15.hospitality")

    @http.route(['/ffe'], type='http', auth="public", website=True)
    def ffe_page(self, **post):
        return request.render("cids_theme_odoo_15.ffe")

    @http.route(['/how_we_design'], type='http', auth="public", website=True)
    def how_we_design_page(self, **post):
        return request.render("cids_theme_odoo_15.how_we_design")
