from django.core.management import BaseCommand

from lib.rugs import import_rugs


class Command(BaseCommand):
    help = 'Import new products to the exiting backend'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def add_products(self, filename):
        print('#' * 80, f'\t Adding products from {filename}', '#' * 80, end='\n')
        import_rugs(filename)

    def handle(self, *args, **options):
        self.add_products(options['filename'])