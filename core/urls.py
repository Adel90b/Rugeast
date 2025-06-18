from django.urls import path
from django.views.generic import TemplateView

from apps.catalogue.views import ProductPicListView
from core import handler

urlpatterns = [
    path('', TemplateView.as_view(template_name='oscar/home/index.html'), name='home'),
    path('terms-and-conditions/', TemplateView.as_view(template_name='oscar/pages/terms_and_conditions.html'), name='terms-and-conditions'),
    path('imprint/', TemplateView.as_view(template_name='oscar/pages/imprint.html'), name='imprint'),
    path('privacy-policy/', TemplateView.as_view(template_name='oscar/pages/privacy_policy.html'), name='privacy-policy'),
    # path('page/privacy-policy2/', TemplateView.as_view(template_name='oscar/pages/privacy_policy2.html'), name='privacy-policy2'),
    # path('page/legal-notice/', TemplateView.as_view(template_name='oscar/pages/legal_notice.html'), name='legal-notice'),
    path('return-policy/', TemplateView.as_view(template_name='oscar/pages/return_policy.html'), name='return-policy'),
    path('faq/', TemplateView.as_view(template_name='oscar/pages/faq.html'), name='faq'),

    path('sitemap-product.xml', handler.sitemap_product, name='sitemap-product'),
    path('sitemap-products.xml', handler.sitemap_products, name='sitemap-products'),
    path('robots.txt', handler.robots, name='robots'),


    path('gallery/', ProductPicListView.as_view(), name='gallery'),

    # path('403/', handler.permission_denied),
    # path('404/', handler.page_not_found),
    # path('500/', handler.server_error),


]