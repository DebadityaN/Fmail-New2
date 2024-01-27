from django.apps import AppConfig


class FmailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fmail'

    def ready(self):
        from . import signals
