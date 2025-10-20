from odoo import models, fields 


class HrHospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Doctor Name', required=True)
    specialty = fields.Char(string='Specialty')
    phone = fields.Char(string='Phone')
    years_of_experience = fields.Integer(string='Years of Experience')
    contact_number = fields.Char(string='Contact Number')
    email = fields.Char(string='Email')
    available = fields.Boolean(string='Available', default=True)