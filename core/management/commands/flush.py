from django.core.management import BaseCommand

from oscar.apps.catalogue.models import AttributeOptionGroup, AttributeOption, \
    ProductClass, ProductAttribute, Product, \
    Category
from oscar.apps.partner.models import Partner, StockRecord


class Command(BaseCommand):
    help = 'Init project and Set all default configurations automatically'

    def handle(self, *args, **options):
        AttributeOptionGroup.objects.all().delete()
        AttributeOption.objects.all().delete()
        ProductAttribute.objects.all().delete()
        Product.objects.all().delete()
        ProductClass.objects.all().delete()
        Partner.objects.all().delete()
        StockRecord.objects.all().delete()
        Category.objects.all().delete()