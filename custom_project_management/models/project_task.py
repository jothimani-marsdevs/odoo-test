from odoo import models, fields, api, _


class ProjectTask(models.Model):
    _name = 'project.task'
    _description = 'Project Task'

    name = fields.Char(
        string='Task Name',
        required=True,
        copy=False,
        help='The title of the task.'
    )
    description = fields.Html(
        string='Task Description',
        help='Detailed description of the task.'
    )
    date_deadline = fields.Date(
        string='Deadline',
        help='The due date for this task.'
    )
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        help='The project this task belongs to.'
    )
    user_id = fields.Many2one(
        'res.users',
        string='Assignee',
        help='The user assigned to complete this task.'
    )
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('in_progress', 'In Progress'),
            ('done', 'Done')
        ],
        string='Status',
        default='draft',
        help='The current status of the task.'
    )

    @api.onchange('user_id')
    def _onchange_user_id(self):
        if self.user_id and self.state == 'draft':
            self.state = 'in_progress'
