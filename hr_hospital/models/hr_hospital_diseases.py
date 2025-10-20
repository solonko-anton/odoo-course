from odoo import models, fields


class HrHospitalDiseases(models.Model):
    _name = 'hr.hospital.diseases'
    _description = 'Hospital Diseases'

    name = fields.Char(string='Disease Name', required=True)
    description = fields.Text(string='Description')
    symptoms = fields.Text(string='Symptoms')
    treatment = fields.Text(string='Treatment')
    contagious = fields.Boolean(string='Contagious', default=False)