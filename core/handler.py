import math

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

# HTTP Error 404
def page_not_found(request, exception):
    response = render('oscar/404.html', status=404)
    response.status_code = 404
    return response

# HTTP Error 403
def permission_denied(request, exception):
    response = render('oscar/403.html', status=403)
    response.status_code = 403
    return response

# HTTP Error 500
def server_error(request):
    response = render('oscar/500.html', status=500)
    # response.status_code = 500
    return response

def offer_round(value, currency):
    return math.ceil(value)

def sitemap_product(request):
    return render('oscar/pages/sitemap-product.xml', content_type='text/xml')
    # return HttpResponse(open('oscar/pages/sitemap-product.xml').read(), content_type='text/xml')

def sitemap_products(request):
    return render('oscar/pages/sitemap-products.xml', content_type='text/xml')
    # return HttpResponse(open('oscar/pages/Sitemap-products.xml').read(), content_type='text/xml')

def robots(request):
    return render('oscar/pages/robots.txt', content_type='text/plain')
    # return HttpResponse(open('oscar/pages/robots.txt').read(), content_type='text/plain')