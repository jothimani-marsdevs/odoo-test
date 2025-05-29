# Odoo Project Management Module

A comprehensive project management module for Odoo 15.0 that enhances the default project management capabilities with advanced features, custom workflows, and improved team collaboration.

## Table of Contents
- [Overview](#overview)
- [Technical Architecture](#technical-architecture)
- [Detailed Setup Guide](#detailed-setup-guide)
- [Module Features](#module-features)
- [Development Guide](#development-guide)
- [API Documentation](#api-documentation)
- [Troubleshooting](#troubleshooting)

## Overview

This custom Odoo module provides an enhanced project management experience with:
- Configurable project workflows
- Advanced task management
- Team collaboration features
- Custom API endpoints
- Automated business logic
- Role-based access control

## Technical Architecture

### Technology Stack
- **Odoo Version**: 15.0
- **Database**: PostgreSQL 13
- **Container Runtime**: Docker & Docker Compose
- **Programming Language**: Python 3.8+
- **Web Framework**: Odoo Framework
- **ORM**: Odoo ORM
- **Frontend**: JavaScript, XML, QWeb templates

### Module Structure
```
custom_project_management/
├── models/                 # Python model definitions
│   ├── project.py         # Project model extensions
│   ├── task.py           # Task model customizations
│   └── stage.py          # Stage configurations
├── controllers/           # API endpoints
│   └── main.py           # REST API implementations
├── security/             # Access rights and rules
│   ├── ir.model.access.csv
│   └── security_rules.xml
├── views/                # UI definitions
│   ├── project_views.xml
│   ├── task_views.xml
│   └── menu_items.xml
├── data/                 # Default data
│   └── default_stages.xml
└── __manifest__.py       # Module manifest
```

## Detailed Setup Guide

### Prerequisites
1. **System Requirements**:
   - Linux/Unix-based system (recommended)
   - Docker Engine 20.10+
   - Docker Compose 2.0+
   - 4GB RAM minimum
   - 10GB free disk space

2. **Port Requirements**:
   - 8069: Odoo web interface
   - 5432: PostgreSQL (internal)

### Step-by-Step Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jothimani-marsdevs/odoo-test.git
   cd odoo-test
   ```

2. **Environment Configuration**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` file with your settings:
   - `ODOO_PORT`: Web interface port (default: 8069)
   - `DB_PASSWORD`: Set a secure database password
   - `ODOO_ADMIN_PASSWORD`: Set admin password
   - See `.env.example` for all available options

3. **Build and Start Services**:
   ```bash
   docker-compose build
   docker-compose up -d
   ```

4. **First-time Setup**:
   - Access `http://localhost:8069`
   - Create database:
     - Master Password: (from ODOO_ADMIN_PASSWORD)
     - Database Name: (from DB_NAME)
     - Email: admin
     - Password: (set a secure password)
   - The module will be automatically installed

5. **Verify Installation**:
   - Login as admin
   - Navigate to Apps
   - Search for "Project Management"
   - Verify module is installed and active

### Post-Installation Configuration

1. **Configure Project Stages**:
   - Navigate to Project > Configuration > Stages
   - Default stages are pre-configured
   - Add/modify stages as needed

2. **Set Up User Access**:
   - Go to Settings > Users & Companies
   - Create users and assign roles:
     - Project Manager
     - Project User

## API Documentation

### Available Endpoints

1. **Get Project Tasks**:
   ```bash
   curl -X POST http://localhost:8069/project/{project_id} \
     -H "Content-Type: application/json" \
     -d '{}'
   ```

2. **Update Task Stage**:
   ```bash
   curl -X POST http://localhost:8069/task/{task_id}/done \
     -H "Content-Type: application/json" \
     -d '{}'
   ```

## Docker Environment Details

### Container Configuration
- **Odoo Container**:
  - Port: 8069 (configurable)
  - Custom addons path: /mnt/extra-addons
  - Config file: /etc/odoo
  
- **PostgreSQL Container**:
  - Version: 13
  - Credentials in `.env`
  - Persistent volume
