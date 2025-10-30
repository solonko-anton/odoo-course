from odoo import models, fields


class HrHospitalDiseases(models.Model):
    _name = 'hr.hospital.diseases'
    _description = 'Hospital Diseases'

    name = fields.Char(required=True)
    description = fields.Text()
    symptoms = fields.Text()
    treatment = fields.Text()
    contagious = fields.Boolean(default=False)