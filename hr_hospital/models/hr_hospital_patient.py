from odoo import models, fields


class HrHospitalDiseases(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        string='Gender'
    )
    contact_number = fields.Char(string='Contact Number')
    address = fields.Text(string='Address')
    