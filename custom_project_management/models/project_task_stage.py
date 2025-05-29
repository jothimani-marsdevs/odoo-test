from odoo import models, fields, api


class ProjectTaskStage(models.Model):
    _name = 'project.task.stage'
    _description = 'Task Stage'
    _order = 'sequence, name'

    @api.model
    def _get_default_project_ids(self):
        default_project_id = self.env.context.get('default_project_id')
        return [default_project_id] if default_project_id else []

    name = fields.Char(string='Stage Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    fold = fields.Boolean(string='Folded in Kanban')
    project_ids = fields.Many2many(
        'project.project',
        'project_stage_rel',
        'stage_id',
        'project_id',
        string='Projects',
        default=lambda self: self._get_default_project_ids()
    )
    is_in_progress = fields.Boolean(string='Is In Progress Stage')
    is_done = fields.Boolean(string='Is Done Stage')
