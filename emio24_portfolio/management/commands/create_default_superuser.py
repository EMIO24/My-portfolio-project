import os
    from django.core.management.base import BaseCommand
    from django.contrib.auth import get_user_model

    class Command(BaseCommand):
        help = 'Creates a default superuser if one does not exist.'

        def handle(self, *args, **options):
            User = get_user_model()
            username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin') # Get from env or default
            email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com') # Get from env or default
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD') # MUST be from env

            if not password:
                self.stdout.write(self.style.ERROR(
                    "DJANGO_SUPERUSER_PASSWORD environment variable not set. Superuser not created."
                ))
                return

            if User.objects.filter(username=username).exists():
                self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' already exists. Skipping creation."))
            else:
                try:
                    User.objects.create_superuser(username=username, email=email, password=password)
                    self.stdout.write(self.style.SUCCESS(f"Successfully created superuser: {username}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error creating superuser: {e}"))

    