import logging

from odoo import http
from odoo.exceptions import AccessError, MissingError
from odoo.http import Controller, route, request

_logger = logging.getLogger(__name__)


class ProjectManagement(Controller):

    @route('/project/<int:project_id>', type='json', auth='public')
    def get_tasks(self, project_id):
        """Fetch all tasks for a given project ID"""
        tasks = request.env['project.task'].sudo().search_read(
            [('project_id', '=', project_id)],
            ['id', 'name', 'description', 'date_deadline', 'stage_id', 'user_id']
        )
        return {'status': 'success', 'tasks': tasks}

    @route('/task/<int:task_id>/done', type='json', auth='public', methods=['POST'])
    def mark_task_done(self, task_id):
        """Mark a specific task as 'done' by updating its stage_id"""
        try:
            task = request.env['project.task'].sudo().browse(task_id)
            if not task.exists():
                raise MissingError(f"Task with ID {task_id} not found.")
            if not task.project_id:
                raise MissingError(f"Task {task.name} has no associated project.")

            done_stage = request.env['project.task.stage'].sudo().search([
                ('is_done', '=', True),
                ('project_ids', 'in', task.project_id.id)
            ], limit=1)

            if not done_stage:
                raise MissingError(
                    f"No 'Done' stage found for project '{task.project_id.name}'. Please configure a stage with is_done=True."
                )

            task.stage_id = done_stage
            return {'status': 'success', 'message': f'Task {task.name} moved to Done stage.'}

        except (AccessError, MissingError) as e:
            _logger.error("Error marking task done: %s", e)
            return {'status': 'error', 'message': str(e)}
