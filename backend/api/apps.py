from django.apps import AppConfig
import threading
from .tasks import background_task


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        if hasattr(self,'already-run'):
            return 
        self.already_run =True 
        thread=threading.Thread(target=background_task)
        thread.daemon=True 
        thread.start()