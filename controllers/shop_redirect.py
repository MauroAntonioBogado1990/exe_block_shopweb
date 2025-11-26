from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleRedirect(WebsiteSale):

    @http.route(['/shop', '/shop/page/<int:page>'], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', **kwargs):
        # Si no hay usuario logueado, redirige al login
        if not request.session.uid:
            return request.redirect('/web/login')
        # Si está logueado, llamamos al controlador original
        return super().shop(page=page, category=category, search=search, **kwargs)