from odoo import models, fields, api

class AttendanceRecord(models.Model):
    _name = 'serata.attendance'
    _description = 'Employee Attendance Record'

    employee_name = fields.Many2one('hr.employee', string="Employee", required=True)
    employee_text = fields.Char(string="Employee Text")
    date = fields.Date(string="Date", required=True)
    in_time = fields.Float(string="In Time")  
    out_time = fields.Float(string="Out Time")  
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent')
    ], string="Status", required=True)
    tttt = fields.Char(string="TT")
    


