from django.core.management import BaseCommand

from lib.rugs import import_images

from oscar.apps.catalogue.models import Product


class Command(BaseCommand):
    help = 'Delete the images of all products and import them again'

    def handle(self, *args, **options):
        for product in Product.objects.all():
            product.images.all().delete()
            import_images(product)