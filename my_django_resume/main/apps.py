from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_django_resume.main'

    def ready(self):
        from . import signals
