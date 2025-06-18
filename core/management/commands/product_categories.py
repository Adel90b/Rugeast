from time import sleep

import requests
from django.core.management import BaseCommand

from apps.catalogue.models import Product


class Command(BaseCommand):
    help = 'cached all of products images'

    def handle(self, *args, **options):
        products = Product.objects.all()
        all_products_counter = products.count()
        counter = 0
        with open('myfile.txt', 'w') as file:
            for product in products:
                cats = product.categories.all()
                if cats.count() > 1:
                    continue
                else:
                    if cats[0].depth != 1:
                        continue
                    if cats[0].slug == 'Antique-Rugs':
                        continue
                cats_str = ''
                for cat in cats:
                    cats_str+= f' {cat.name}/{cat.slug}/d:{cat.depth} |'
                file.write(f'{product.upc}: {cats_str}\n')
                counter += 1
            file.write(f'products_counter: {all_products_counter} | counter: {counter}')