from time import sleep

import requests
from celery import shared_task
from celery.schedules import crontab

from django.contrib.auth import get_user_model
from oscar.apps.order.processing import EventHandler
from oscar.core.loading import get_model

from apps.catalogue.functions import file_ebay, file_google, file_amazon
# from apps.importer.models import ExportData
from apps.order.models import Order
from teemche.celery import app



User = get_user_model()
Product = get_model('catalogue', 'Product')
Category = get_model('catalogue', 'Category')
ExportData = get_model('importer', 'ExportData')
ConditionalOffer = get_model('offer', 'ConditionalOffer')

# @periodic_task(run_every=crontab(minute=0, hour=1))
# def render_images():
#     base = 'https://rugeast.com'
#     for product in Product.objects.all():
#         try:
#             _ = requests.get(base + product.get_absolute_url())
#         except:
#             pass

@shared_task
def set_off():
    all_products = Product.objects.all()
    all_products.update(offer_value=0.00)
    offers = ConditionalOffer.objects.all().order_by('priority')
    for offer in offers:
        if offer.is_open and offer.has_products and offer.is_available() and not offer.is_voucher_offer_type:
            products = offer.products()
            if products.exists():
                products.update(offer_value=offer.benefit.value)
            else:
                continue
# Schedule the task to run every day at 3 AM
app.conf.beat_schedule = {
    'set_off': {
        'task': 'tasks.set_off',
        'schedule': crontab(hour='02', minute='00')
    }
}

@shared_task
def set_product_offer():
    str = ''
    str += 'set_product_offer \n'
    all_products = Product.objects.all()
    all_products.update(offer_value=0.00)
    offers = ConditionalOffer.objects.all().order_by('priority')
    for offer in offers:
        if offer.is_open and offer.has_products and offer.is_available() and not offer.is_voucher_offer_type:
            products = offer.products()
            if products.exists():
                str += f'Offer: {offer} | products: {products.count()} \n'
                products.update(offer_value=offer.benefit.value)
            else:
                continue
    return str

@shared_task
def cancel_order(order_id):
    try:
        order = Order.objects.get(pk=order_id)
        if order.status == 'Pending' or order.status == 'New':
            for line in order.lines.all():
                line.stockrecord.cancel_allocation(line.quantity)
            order.set_status('Expired')
            order.basket.status = 'Submitted'
            order.basket.save()
    except Order.DoesNotExist:
        print(f"Order with id {order_id} does not exist.")


@app.task
def ex_ebay(object_id):
    try:
        sleep(5)
        obj = ExportData.objects.get(pk=object_id)
        queryset = Product.objects.all()
        url = file_ebay(request=None, queryset=queryset)
        obj.url = url
        obj.save()
        return url
    except Exception as e:
        return print(f"{e}.")


@app.task
def ex_google(object_id):
    try:
        sleep(5)
        obj = ExportData.objects.get(pk=object_id)
        queryset = Product.objects.all()
        url = file_google(request=None, queryset=queryset)
        obj.url = url
        obj.save()
        return url
    except Exception as e:
        return print(f"{e}.")


@app.task
def ex_amazon(object_id):
    try:
        sleep(5)
        obj = ExportData.objects.get(pk=object_id)
        modern_carpet_category = Category.get_root_nodes().get(slug='modern-carpets')
        modern_carpet_children_slug = modern_carpet_category.get_children().values_list("slug", flat=True)
        slug_list = list(modern_carpet_children_slug)
        slug_list.append('modern-carpets')
        queryset = Product.objects.filter(categories__slug__in=slug_list).distinct()
        # queryset = Product.objects.filter(categories__slug='modern-carpets')
        url = file_amazon(request=None, queryset=queryset)
        obj.url = url
        obj.save()
        return url
    except Exception as e:
        return print(f"{e}.")


# @shared_task

@app.task
def cached_images(queryset):
    base = 'https://rugeast.com'
    data = {
        'success_id': [],
        'failure_id': [],
    }
    for product in queryset:
        try:
            _ = requests.get(base + product.get_absolute_url())
            if _.status_code == 200:
                data['success_id'].append(product.id)
            else:
                data['failure_id'].append(product.id)
        except:
            data['failure_id'].append(product.id)
    return data


@app.task
def cached_single_images(upc):
    product = Product.objects.get(upc=upc)
    base = 'https://rugeast.com'
    url = base + product.get_absolute_url()
    try:
        _ = requests.get(url)
        if _.status_code == 200:
            return f'UPC: {product.upc} | Done | url: {url} '

        else:
            return f'UPC: {product.upc} | Res error | url: {url}'
    except:
        return f'UPC: {product.upc} | Try error | url: {url}'