from __future__ import annotations

CSS_PATH = "static/test.css"

COOKIECUTTER_TEMPLATE_URL = "https://github.com/godd0t/streamline-cookiecutter"

PROJECT_TYPE_OPTIONS = [
    {"name": "Django", "id": "django", "value": True},
    {"name": "Domain Driven Design", "id": "ddd", "value": False},
]

USE_SERVICE_ANSWERS = [
    {"name": "No", "id": "no", "value": True},
    {"name": "Yes", "id": "yes", "value": False},
]

PROJECT_INFO_INPUTS = [
    {"name": "Project Name", "id": "project_name"},
    {"name": "Project Description", "id": "project_description"},
    {"name": "App Name", "id": "app_name"},
]


USE_SERVICE_TYPES = [
    "celery",
    "celerybeat",
    "django",
    "django-celery-beat",
]
