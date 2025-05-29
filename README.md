# Odoo Project & Task Management

A custom module for Odoo 15 that enhances project and task management capabilities with configurable stages, access control, kanban support, and smart business logic.

---

## 🔧 Features

### ✅ Project Management
- Create and manage projects with a start and end date.
- Assign a project manager.
- Smart button to view related tasks.
- Automatically computed task statistics (total and completed).
- Prevent deletion of projects with existing tasks.

### ✅ Task Management
- Create tasks with project, deadline, user, and stage.
- Stages are project-specific and configurable via many2many relation.
- Automatic status update to "In Progress" when assignee is set.
- Chatter integration for tasks and projects.
- Stage-wise Kanban support with fold and statusbar functionality.

### ✅ Task Stages
- Custom model `project.task.stage` with:
  - Project-wise many2many relationship.
  - Booleans for `is_in_progress` and `is_done`.
  - Fold field to manage Kanban UI behavior.
- Automatically sets default stage based on context (`default_project_id`).

### ✅ Security & Access Control
- Only project managers can create/edit/delete projects.
- Any authenticated user can view projects and tasks.
- Fully configured `ir.model.access.csv`.

---

## 🚀 Installation

1. Clone this repository into your Odoo addons directory:

```bash
git clone https://github.com/jothimani-marsdevs/odoo-test.git
```

## Test API
1.Get all tasks from specific project
```bash
curl -X POST http://localhost:8069/project/2 \
  -H "Content-Type: application/json" \
  -d '{}'
```
2.Mark as done a stage
```bash
curl -X POST http://localhost:8069/task/42/done \
  -H "Content-Type: application/json" \
  -d '{}'
```