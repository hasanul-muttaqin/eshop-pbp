from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        # tambah sesuatu di local buat trobleshoot
        from django.core.management import call_command
        try:
            call_command("migrate", interactive=False)
        except Exception as e:
            print("Migration failed:", e)
