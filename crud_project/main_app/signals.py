from django.db.models.signals import post_migrate
from django.core.management import call_command
from django.dispatch import receiver
from .models import Ciudad

@receiver(post_migrate)
def load_initial_data(sender, **kwargs):
    if not Ciudad.objects.exists():
        call_command('loaddata', 'main_app/fixtures/initial_data.json')