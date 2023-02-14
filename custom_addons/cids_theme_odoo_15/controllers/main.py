from odoo.http import request
from odoo import http


class DemoClass(http.Controller):

    @http.route(['/'], type='http', auth="user", website=True)
    def home_page(self, **post):
        return request.render("cids_theme_odoo_15.home")

    @http.route(['/landing'], type='http', auth="user", website=True)
    def landing_page(self, **post):
        return request.render("cids_theme_odoo_15.landing_page")

    @http.route(['/commercial'], type='http', auth="user", website=True)
    def commercial_page(self, **post):
        return request.render("cids_theme_odoo_15.commercial")

    @http.route(['/hospitality'], type='http', auth="user", website=True)
    def hospitality_page(self, **post):
        return request.render("cids_theme_odoo_15.hospitality")

    @http.route(['/ffe'], type='http', auth="user", website=True)
    def ffe_page(self, **post):
        return request.render("cids_theme_odoo_15.ffe")

    @http.route(['/how_we_design'], type='http', auth="user", website=True)
    def how_we_design_page(self, **post):
        return request.render("cids_theme_odoo_15.how_we_design")

    @http.route(['/about'], type='http', auth="user", website=True)
    def about_page(self, **post):
        return request.render("cids_theme_odoo_15.about")

    @http.route(['/our_principles'], type='http', auth="user", website=True)
    def our_principles_page(self, **post):
        return request.render("cids_theme_odoo_15.our_principles")

    @http.route(['/cids_contactus'], type='http', auth="public", website=True)
    def contactus_page(self, **post):
        return request.render("cids_theme_odoo_15.cids_contactus")

    @http.route(['/cids_contact_us'], method='POST', type='http', auth="public", website=True)
    def cids_contactus_page(self, **post):
        vals = {
            'contact_name': post.get('contact_name'),
            'phone': post.get('phone'),
            'email_from': post.get('email_from'),
            'partner_name': post.get('partner_name'),
            'name': post.get('name'),
            'type': 'opportunity',
            'description': post.get('description')
        }
        crm = request.env['crm.lead'].sudo().create(vals)
        print(crm)
        values = {
            'lead': crm
        }
        return request.render('website.contactus_thanks', values)
