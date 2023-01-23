# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.TransientModel):
    _name = 'subcontractor.purchase.order'

    partner_id = fields.Many2one(
        'res.partner',
        string="Vendor / Subcontractor",
        required=True,
    )

    # @api.multi #odoo13
    def create_purchase_order(self):
        task_id = self._context.get('active_id', False)
        task = self.env['project.task'].browse(task_id)
        order_line = self.env['purchase.order.line']

        purchaseorder = {
            'partner_id': self.partner_id.id,
            'date_order': fields.date.today(),
            'subcontractor_id': task_id,
        }

        purchase_order = self.env['purchase.order'].create(purchaseorder)
        for line in task.purchaseorder_line_ids:
            if not line.is_created:
                line_vals = {
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.quantity,
                }
                new_line = self.env['purchase.order.line'].new(line_vals)
                new_line.onchange_product_id()
                line_vals_dict = self.env['purchase.order.line']._convert_to_write({
                    name: new_line[name] for name in new_line._cache
                })

                line_vals_dict.update({
                    'job_cost_id': line.job_cost_id.id, 
                    'job_cost_line_id': line.job_cost_line_id.id,
                    'order_id': purchase_order.id
                })

                order_line.create(line_vals_dict)
                line.write({'is_created': True})

        res = self.env.ref('purchase.purchase_rfq')
        res = res.sudo().read()[0]
        res['domain'] = str([('id', '=', purchase_order.id)])
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
