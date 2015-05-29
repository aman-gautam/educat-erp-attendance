# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Attendance(models.Model):
    _inherit = 'op.attendance.sheet'

    def _test_change(self):
        if self.register_id:
            list_lines = []
            result = {'value': {}}

            student_model = self.env['op.student']
            student_ids = student_model.search([
                ('division_id', '=', self.register_id.division_id.id),
                ('course_id', '=', self.register_id.course_id.id),
                ('batch_id', '=', self.register_id.batch_id.id),
                ('standard_id', '=', self.register_id.standard_id.id),
            ])

            for student_id in student_ids:
                #http://dirtyhandsphp.blogspot.in/2014/11/odooopenerp-populate-one2many-list.html
                # Create a new attendance line.
                list_lines.append({
                    'student_id': student_id,
                    'present': False,
                    'course_id': self.register_id.course_id.id,
                    'standard_id': self.register_id.standard_id.id,
                    'division_id': self.register_id.division_id.id,
                    'attendance_date': fields.Date.today()
                })
            result['value']['attendance_line'] = list_lines
            return result

    @api.one
    def generate_students(self, *args, **kwargs):
        result = self._test_change()
        self.attendance_line = result['value']['attendance_line']



class User(models.Model):
    _inherit = 'res.partner'

    # This GCM id can be used to send the mobile device some push message
    # based on certain events...
    gcm_id = fields.Char()


class Feedback(models.Model):
    _name = 'attendance.feedback'

    _inherit = 'mail.thread'

    name = fields.Char(compute='_compute_name')
    author = fields.Many2one('op.student', string='Student')
    rating = fields.Integer()
    comment = fields.Text()
    target = fields.Many2one('op.faculty', string='Faculty')

    def _compute_name(self):
        self.name = self.author.name + self.target.name