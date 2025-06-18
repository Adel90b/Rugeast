from django.core.management import BaseCommand

from oscar.apps.partner.models import StockRecord


class Command(BaseCommand):
    help = 'Init project and Set all default configurations automatically'

    def handle(self, *args, **options):
        StockRecord.objects.all().update(price_currency='EUR')