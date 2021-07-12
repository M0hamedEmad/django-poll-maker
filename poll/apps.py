from django.apps import AppConfig


class PollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'poll'
    
    def ready(self):
        import poll.signals