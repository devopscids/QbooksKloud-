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

    @http.route(['/cids_thankyou'], type='http', auth="public", website=True)
    def contactus_thankyou_page(self, **post):
        return request.render("cids_theme_odoo_15.cids_thankyou")

    @http.route(['/site_map'], type='http', auth="public", website=True)
    def site_map_page(self, **post):
        return request.render("cids_theme_odoo_15.site_map")

    @http.route(['/team'], type='http', auth="public", website=True)
    def team_page(self, **post):
        return request.render("cids_theme_odoo_15.team")

    @http.route(['/team-detail-vk'], type='http', auth="public", website=True)
    def team_detail_page(self, **post):
        partner_id = request.env['res.partner'].sudo().search([('name', '=', 'Vijay Kapoor')])
        data = request.env['blog.post'].sudo().search([('author_id', '=', partner_id.id)], order='create_date desc')
        values = {}
        data_set = []
        for i in data:
            url = i.cover_properties
            res = eval(url)
            url_data = res.get('background-image').replace("url('", "")
            data_set.append({
                'name': i.name,
                'teaser': i.teaser,
                'blog_id': i.blog_id.id,
                'id': i.id,
                'url': url_data.replace("')", "")
            })
        values = {
            'data': data_set
        }
        print(values)
        return request.render("cids_theme_odoo_15.team-detail", values)

    @http.route(['/team-detail-rb'], type='http', auth="public", website=True)
    def team_detail_page_rb(self, **post):
        partner_id = request.env['res.partner'].sudo().search([('name', '=', 'Reshma Bhakta')])
        data = request.env['blog.post'].sudo().search([('author_id', '=', partner_id.id)], order='create_date desc')
        values = {}
        data_set = []
        for i in data:
            url = i.cover_properties
            res = eval(url)
            url_data = res.get('background-image').replace("url('", "")
            data_set.append({
                'name': i.name,
                'teaser': i.teaser,
                'blog_id': i.blog_id.id,
                'id': i.id,
                'url': url_data.replace("')", "")
            })
        values = {
            'data': data_set
        }
        print(values)
        return request.render("cids_theme_odoo_15.team-detail2", values)

    @http.route(['/team-detail-ha'], type='http', auth="public", website=True)
    def team_detail_page_ha(self, **post):
        partner_id = request.env['res.partner'].sudo().search([('name', '=', 'Hanan Alshakhrit')])
        data = request.env['blog.post'].sudo().search([('author_id', '=', partner_id.id)], order='create_date desc')
        values = {}
        data_set = []
        for i in data:
            url = i.cover_properties
            res = eval(url)
            url_data = res.get('background-image').replace("url('", "")
            data_set.append({
                'name': i.name,
                'teaser': i.teaser,
                'blog_id': i.blog_id.id,
                'id': i.id,
                'url': url_data.replace("')", "")
            })
        values = {
            'data': data_set
        }
        print(values)
        return request.render("cids_theme_odoo_15.team-detail3", values)

    @http.route(['/team-detail-pp'], type='http', auth="public", website=True)
    def team_detail_page_pp(self, **post):
        partner_id = request.env['res.partner'].sudo().search([('name', '=', 'Pravin Patel')])
        data = request.env['blog.post'].sudo().search([('author_id', '=', partner_id.id)], order='create_date desc')
        values = {}
        data_set = []
        for i in data:
            url = i.cover_properties
            res = eval(url)
            url_data = res.get('background-image').replace("url('", "")
            data_set.append({
                'name': i.name,
                'teaser': i.teaser,
                'blog_id': i.blog_id.id,
                'id': i.id,
                'url': url_data.replace("')", "")
            })
        values = {
            'data': data_set
        }
        print(values)
        return request.render("cids_theme_odoo_15.team-detail4", values)

    @http.route(['/team-detail-mb'], type='http', auth="public", website=True)
    def team_detail_page_mb(self, **post):
        partner_id = request.env['res.partner'].sudo().search([('name', '=', 'Mukesh Bhakta')])
        data = request.env['blog.post'].sudo().search([('author_id', '=', partner_id.id)], order='create_date desc')
        values = {}
        data_set = []
        for i in data:
            url = i.cover_properties
            res = eval(url)
            url_data = res.get('background-image').replace("url('", "")
            data_set.append({
                'name': i.name,
                'teaser': i.teaser,
                'blog_id': i.blog_id.id,
                'id': i.id,
                'url': url_data.replace("')", "")
            })
        values = {
            'data': data_set
        }
        print(values)
        return request.render("cids_theme_odoo_15.team-detail5", values)

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
        return request.redirect('/cids_thankyou')
        # return request.render('website.contactus_thanks', values)
