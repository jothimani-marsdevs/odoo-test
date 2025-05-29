from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class Project(models.Model):
    _name = 'project.project'
    _inherit = ['mail.thread', 'mail.activity.mixin']
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
        required=True,
        help='The planned start date of the project.'
    )
    date_end = fields.Date(
        string='End Date',
        required=True,
        help='The planned end date of the project.'
    )
    user_id = fields.Many2one(
        'res.users',
        string='Project Manager',
        required=True,
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
    task_stage_ids = fields.Many2many(
        'project.task.stage',
        'project_stage_rel',
        'project_id',
        'stage_id',
        string='Task Stages'
    )

    @api.depends('task_ids.stage_id')
    def _compute_task_stats(self):
        for project in self:
            project.task_count = len(project.task_ids)
            project.completed_task_count = len(
                project.task_ids.filtered(lambda t: t.stage_id.name == 'Done')
            )

    def unlink(self):
        for project in self:
            if project.task_ids:
                raise ValidationError(_("Cannot delete a project that has tasks."))
        return super(Project, self).unlink()

    def action_view_all_tasks(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Al Tasks',
            'view_mode': 'kanban,tree,form',
            'res_model': 'project.task',
            'domain': [('project_id', '=', self.id)],
            'context': {'default_project_id': self.id},
        }

    def action_view_completed_tasks(self):
        self.ensure_one()

        done_stage = self.env['project.task.stage'].search([
            ('is_done', '=', True),
            ('project_ids', 'in', self.id)
        ], limit=1)

        if not done_stage:
            raise UserError(_('No "Done" stage is configured for this project. Please define one in Task Stages.'))

        domain = [
            ('project_id', '=', self.id),
            ('stage_id', '=', done_stage.id)
        ]

        return {
            'type': 'ir.actions.act_window',
            'name': 'Completed Tasks',
            'view_mode': 'kanban,tree,form',
            'res_model': 'project.task',
            'domain': domain,
            'context': {'default_project_id': self.id},
        }
