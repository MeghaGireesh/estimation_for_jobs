from odoo import fields, models, api


class Estimation(models.Model):
    _name = 'estimation.jobs'

    customer_id = fields.Many2one('res.partner', string="Customer")
    price_list_id = fields.Many2one('product.pricelist', string="Price list")
    payment_terms_id = fields.Many2one('account.payment.term',
                                       string="Payment Terms")
    # customer_reference = fields.Char(string="Customer Reference")
    date = fields.Date(string="Date")
    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env.company)
    # currency=
    project_id = fields.Many2one('project.project', string='Project')
    analytic_account = fields.Many2one('account.analytic.account',
                                       string="Analytic Account")
    job_types = fields.Many2many('job.type', string="Job Types")
    material_estimation_ids = fields.One2many('material.estimation',
                                              'connection_id')
    labour_estimation_ids = fields.One2many('labour.estimation',
                                            'connection_id')
    overhead_estimation_ids = fields.One2many('overhead.estimation',
                                              'connection_id')

    # source_doc=feilds.Char(string="Source Document Sales Person")
    # sales_team
    # sales_


class MaterialEstimation(models.Model):
    _name = 'material.estimation'

    connection_id = fields.Many2one('estimation.jobs')
    type = fields.Char(string="Type", default='Material')
    product_id = fields.Many2one('product.product', string="Product")
    quantity = fields.Integer(string='Quantity')
    uom = fields.Char(related='product_id.uom_id.name',
                      string='Unit of Measure')
    unit_price = fields.Float(related='product_id.lst_price',
                              string='Unit Price')
    code = fields.Char(related='product_id.default_code',
                       string='Description')

    description = fields.Char(string="Description",
                              compute="_compute_description_")
    subtotal = fields.Float(string="Sub Total")
    discount = fields.Float(string="Discount(%)")

    @api.onchange('quantity', 'unit_price')
    def sub_total(self):
        for rec in self:
            rec.subtotal = rec.quantity * rec.unit_price

    # @api.onchange('discount')
    # def discount(self):
    #     for res in self:
    #         res.subtotal = (res.subtotal * res.discount) / 100 - res.subtotal

    @api.depends('product_id', 'code')
    def _compute_description_(self):
        for field in self:
            product_id = str(field.product_id.name) + " "
            code = str(field.code) + " "
            field.description = product_id + "[" + code + "]"


class LabourEstimation(models.Model):
    _name = 'labour.estimation'

    connection_id = fields.Many2one('estimation.jobs')
    type = fields.Char(string="Type", default='Labour')
    product_id = fields.Many2one('product.product', string="Product")
    quantity = fields.Integer(string='Quantity')
    uom = fields.Char(related='product_id.uom_id.name',
                      string='Unit of Measure')
    unit_price = fields.Float(related='product_id.lst_price',
                              string='Unit Price')
    code = fields.Char(related='product_id.default_code',
                       string='Description')

    description = fields.Char(string="Description",
                              compute="_compute_description_")
    subtotal = fields.Float(string="Sub Total")
    discount = fields.Float(string="Discount(%)")

    @api.onchange('quantity', 'unit_price')
    def sub_total(self):
        for rec in self:
            rec.subtotal = rec.quantity * rec.unit_price

    # @api.onchange('discount')
    # def discount(self):
    #     for res in self:
    #         res.subtotal = (res.subtotal * res.discount) / 100 - res.subtotal

    @api.depends('product_id', 'code')
    def _compute_description_(self):
        for field in self:
            product_id = str(field.product_id.name) + " "
            code = str(field.code) + " "
            field.description = product_id + "[" + code + "]"


class OverheadEstimation(models.Model):
    _name = 'overhead.estimation'

    connection_id = fields.Many2one('estimation.jobs')
    type = fields.Char(string="Type", default='Overhead')
    product_id = fields.Many2one('product.product', string="Product")
    quantity = fields.Integer(string='Quantity')
    uom = fields.Char(related='product_id.uom_id.name',
                      string='Unit of Measure')
    unit_price = fields.Float(related='product_id.lst_price',
                              string='Unit Price')
    code = fields.Char(related='product_id.default_code',
                       string='Description')

    description = fields.Char(string="Description",
                              compute="_compute_description_")
    subtotal = fields.Float(string="Sub Total")
    discount = fields.Float(string="Discount(%)")

    @api.onchange('quantity', 'unit_price')
    def sub_total(self):
        for rec in self:
            rec.subtotal = rec.quantity * rec.unit_price

    # @api.onchange('discount')
    # def discount(self):
    #     for res in self:
    #         res.subtotal = (res.subtotal * res.discount) / 100 - res.subtotal

    @api.depends('product_id', 'code')
    def _compute_description_(self):
        for field in self:
            product_id = str(field.product_id.name) + " "
            code = str(field.code) + " "
            field.description = product_id + "[" + code + "]"


class JobType(models.Model):
    _name = 'job.type'

    job_type = fields.Char(string="Job Types")
