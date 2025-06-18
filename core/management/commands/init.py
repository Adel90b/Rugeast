from django.core.management import BaseCommand
from django.contrib.sites.models import Site
from oscar.apps.partner.models import Partner

from lib.rugs import create_rugs_type, import_rugs, import_categories


class Command(BaseCommand):
    help = 'Init project and Set all default configurations automatically'

    def add_arguments(self, parser):
        parser.add_argument('site', type=str)
        parser.add_argument('product_type', type=str)

    def configure_site(self, site_name):
        site = Site.objects.get_current()
        site.domain = site_name
        site.name = site_name
        site.save()

    def add_product_type(self, product_type):
        print('#' * 80, '\t Creating product type', '#' * 80, end='\n')
        if product_type == 'rugs':
            return create_rugs_type()
        return None

    def add_products(self, product_type):
        print('#' * 80, '\t Adding products', '#' * 80, end='\n')
        import_rugs()

    def add_partner(self, name):
        return Partner.objects.get_or_create(name=name, code=name.lower())

    def add_categories(self):
        print('#' * 80, '\t Adding categories', '#' * 80, end='\n')
        import_categories()

    def handle(self, *args, **options):
        # Todo: Set site default template
        # Todo: Handle migrations
        # Todo: Handle collectstatics

        self.configure_site(options['site'])
        product_type = self.add_product_type(options['product_type'])
        self.add_categories()
        self.add_partner(options['site'])
        self.add_products(product_type)