from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site

class Command(BaseCommand):
    help = 'Setup site domain untuk OAuth'

    def add_arguments(self, parser):
        parser.add_argument('--domain', default='localhost:8000')

    def handle(self, *args, **options):
        domain = options['domain']
        site, _ = Site.objects.get_or_create(pk=1)
        site.domain = domain
        site.name = 'Kelompok Website'
        site.save()
        self.stdout.write(self.style.SUCCESS(f'Site domain set to: {domain}'))
