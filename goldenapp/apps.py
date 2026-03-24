from django.apps import AppConfig


class GoldenappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goldenapp'

    def ready(self):
    	import goldenapp.signals
