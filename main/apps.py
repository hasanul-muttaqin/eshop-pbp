from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        # Run migrations automatically if tables are missing
        from django.core.management import call_command
        try:
            call_command("migrate", interactive=False)
        except Exception as e:
            print("Migration failed:", e)
