from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Project(models.Model):
    _name = 'project.project'
    _description = 'Project'

    name = fields.Char(
        string='Project Name',
        required=True,
        copy=False,
        help='The title of the project.'
    )
    description = fields.Html(
        string='Project Description',
        help='Detailed description of the project.'
    )
    date_start = fields.Date(
        string='Start Date',
        help='The planned start date of the project.'
    )
    date_end = fields.Date(
        string='End Date',
        help='The planned end date of the project.'
    )
    user_id = fields.Many2one(
        'res.users',
        string='Project Manager',
        help='The user responsible for managing this project.'
    )
    task_ids = fields.One2many(
        'project.task',
        'project_id',
        string='Tasks'
    )
    task_count = fields.Integer(
        string='Total Tasks',
        compute='_compute_task_stats',
        store=True
    )
    completed_task_count = fields.Integer(
        string='Completed Tasks',
        compute='_compute_task_stats',
        store=True
    )

    @api.depends('task_ids.state')
    def _compute_task_stats(self):
        for project in self:
            project.task_count = len(project.task_ids)
            project.completed_task_count = len(
                project.task_ids.filtered(lambda t: t.state == 'done')
            )

    def unlink(self):
        for project in self:
            if project.task_ids:
                raise ValidationError(_("Cannot delete a project that has tasks."))
        return super(Project, self).unlink()
