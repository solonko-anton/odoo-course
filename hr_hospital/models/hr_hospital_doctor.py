from odoo import models, fields 


class HrHospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(required=True)
    specialty = fields.Char()
    phone = fields.Char()
    years_of_experience = fields.Integer()
    contact_number = fields.Char()
    email = fields.Char()
    available = fields.Boolean(default=True)