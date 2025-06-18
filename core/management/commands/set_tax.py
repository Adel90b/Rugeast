from django.core.management import BaseCommand

from oscar.apps.catalogue.models import Product
from oscar.apps.partner.models import StockRecord

from decimal import Decimal as D

# percentage. (example: 10% => D('10.00') or 15.5% => D('15.5'))
INCREASE_TAX = D('19.00')
DECREASE_TAX = D('0.00')


class Command(BaseCommand):
    def handle(self, *args, **options):
        if DECREASE_TAX > D('0.00'):
            self.calculate('decrease')
        if INCREASE_TAX > D('0.00'):
            self.calculate('increase')
        if INCREASE_TAX == D('0.00') and DECREASE_TAX == D('0.00'):
            print('*error: you not set percentage*')
            
    
    def calculate(self, operator):
        products = StockRecord.objects.all()
        if products:
            for p in products:
                record = p
                increase_tax = (INCREASE_TAX * record.price_excl_tax) / 100
                if operator == "increase":
                    increase_tax = (INCREASE_TAX * record.price_excl_tax) / 100
                    record.price_excl_tax = record.price_excl_tax + increase_tax
                    record.save()
                if operator == "decrease":
                    decrease_tax = (DECREASE_TAX * record.price_excl_tax) / 100
                    record.price_excl_tax = record.price_excl_tax - decrease_tax
                    record.save()
            print("*SUCCESS*")
        else:
            print("*error: products doesn't exist.*")