from odoo import models, fields


class HrHospitalDiseases(models.Model):
    _name = 'hr.hospital.patient.visits'
    _description = 'Hospital Patient Visits'

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string='Patient',
        required=True,
        ondelete='cascade'
    )
    visit_date = fields.Datetime(string='Visit Date', required=True)
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor',
        required=True,
        ondelete='cascade'
    )
    disease_ids = fields.Many2many(
        comodel_name='hr.hospital.diseases',
        string='Diseases'
    )