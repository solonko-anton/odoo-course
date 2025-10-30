from odoo import models, fields


class HrHospitalDiseases(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(required=True)
    age = fields.Integer()
    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
    )
    contact_number = fields.Char()
    address = fields.Text()
    