# -*- coding: utf-8 -*-
# from odoo import http


# class LoginLayout(http.Controller):
#     @http.route('/login_layout/login_layout/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/login_layout/login_layout/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('login_layout.listing', {
#             'root': '/login_layout/login_layout',
#             'objects': http.request.env['login_layout.login_layout'].search([]),
#         })

#     @http.route('/login_layout/login_layout/objects/<model("login_layout.login_layout"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('login_layout.object', {
#             'object': obj
#         })
