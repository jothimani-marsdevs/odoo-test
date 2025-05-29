from odoo import models, fields, api, _


class ProjectTask(models.Model):
    _name = 'project.task'
    _description = 'Project Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Task Name', required=True, copy=False, tracking=True)
    description = fields.Html(string='Task Description')
    date_deadline = fields.Date(string='Deadline')
    project_id = fields.Many2one('project.project', string='Project', tracking=True)
    user_id = fields.Many2one('res.users', string='Assignee', tracking=True)

    stage_id = fields.Many2one(
        'project.task.stage',
        string='Status',
        index=True,
        tracking=True,
        compute='_compute_stage_id',
        readonly=False,
        store=True,
        copy=False,
        group_expand='_read_group_stage_ids',
        domain="[('project_ids', '=', project_id)]",
    )

    @api.onchange('user_id')
    def _onchange_user_id(self):
        if self.user_id and self.project_id and self.stage_id:
            if not self.stage_id.is_in_progress:
                progress_stage = self.env['project.task.stage'].search([
                    ('is_in_progress', '=', True),
                    ('project_ids', 'in', self.project_id.id)
                ], limit=1)
                if progress_stage:
                    self.stage_id = progress_stage

    @api.depends('project_id')
    def _compute_stage_id(self):
        for task in self:
            if not task.stage_id and task.project_id:
                default_stage = self.env['project.task.stage'].search([
                    ('project_ids', '=', task.project_id.id)
                ], limit=1)
                task.stage_id = default_stage

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        project_id = self.env.context.get('default_project_id')
        if project_id:
            return self.env['project.task.stage'].search([
                ('project_ids', '=', project_id)
            ], order=order)
        return self.env['project.task.stage'].search([], order=order)
