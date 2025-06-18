import decimal
from collections import OrderedDict

from oscar.defaults import OSCAR_DASHBOARD_NAVIGATION

from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _


import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)




OSCAR_DASHBOARD_NAVIGATION = [
    {
        'label': _('Dashboard'),
        'icon': 'icon-th-list',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Catalogue'),
        'icon': 'icon-sitemap',
        'children': [
            {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
            },
            # {
            #     'label': _('Product Types'),
            #     'url_name': 'dashboard:catalogue-class-list',
            # },
            {
                'label': _('Categories'),
                'url_name': 'dashboard:catalogue-category-list',
            },

            # {
            #     'label': _('Low stock alerts'),
            #     'url_name': 'dashboard:stock-alert-list',
            # },
            # {
            #     'label': _('Options'),
            #     'url_name': 'dashboard:catalogue-option-list',
            # },
        ]
    },
    {
        'label': _('Fulfilment'),
        'icon': 'icon-shopping-cart',
        'children': [
            {
                'label': _('Orders'),
                'url_name': 'dashboard:order-list',
            },
            {
                'label': _('Statistics'),
                'url_name': 'dashboard:order-stats',
            },
            # {
            #     'label': _('Partners'),
            #     'url_name': 'dashboard:partner-list',
            # },
            # The shipping method dashboard is disabled by default as it might
            # be confusing. Weight-based shipping methods aren't hooked into
            # the shipping repository by default (as it would make
            # customising the repository slightly more difficult).
            # {
            #     'label': _('Shipping charges'),
            #     'url_name': 'dashboard:shipping-method-list',
            # },
        ]
    },
    {
        'label': _('Customers'),
        'icon': 'icon-group',
        'children': [
            {
                'label': _('Customers'),
                'url_name': 'dashboard:users-index',
            },
            # {
            #     'label': _('Stock alert requests'),
            #     'url_name': 'dashboard:user-alert-list',
            # },
        ]
    },
    {
        'label': _('Offers'),
        'icon': 'icon-bullhorn',
        'children': [
            {
                'label': _('Offers'),
                'url_name': 'dashboard:offer-list',
            },
            {
                'label': _('Vouchers'),
                'url_name': 'dashboard:voucher-list',
            },
            {
                'label': _('Voucher Sets'),
                'url_name': 'dashboard:voucher-set-list',
            },
            {
                'label': _('Ranges'),
                'url_name': 'dashboard:range-list',
            },
        ],
    },
    # {
    #     'label': _('Content'),
    #     'icon': 'icon-folder-close',
    #     'children': [
    #         {
    #             'label': _('Pages'),
    #             'url_name': 'dashboard:page-list',
    #         },
    #         {
    #             'label': _('Email templates'),
    #             'url_name': 'dashboard:comms-list',
    #         },
    #         {
    #             'label': _('Reviews'),
    #             'url_name': 'dashboard:reviews-list',
    #         },
    #     ]
    # },
    {
        'label': _('Reports'),

        'url_name': 'dashboard:reports-index',
    },
    # {
    #     'label': _('PayPal'),
    #     'icon': 'icon-globe',
    #     'children': [
    #         {
    #             'label': _('Express transactions'),
    #             'url_name': 'express_dashboard:paypal-express-list',
    #         },
    #     ]
    # },
# {
#         'label': _('Home'),
#         'icon': 'icon-home',
#         'children': [
#             {
#                 'label': _('Featured images'),
#                 'url_name': 'admin:slider_featuredimages_changelist',
#                 'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
#             },
#             {
#                 'label': _('Home rows'),
#                 'url_name': 'admin:slider_homepage_changelist',
#                 'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
#             },
#          ]
#     }, {
#         'label': _('Extra'),
#         'icon': 'icon-globe',
#         'children': [
#             {
#                 'label': _('Social links'),
#                 'url_name': 'admin:social_sociallink_changelist',
#                 'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
#             },
#             {
#                 'label': _('Contacts data'),
#                 'url_name': 'admin:social_contactlink_changelist',
#                 'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
#             },
#          ]
#     },
    {
        'label': _('Importer'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('Bulk product import'),
                'url_name': 'csv_import_file_products',
                'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            },
            # {
            #     'label': _('Bulk status update'),
            #     'url_name': 'csv_import_file_product_edit',
            #     'access_fn': lambda user, url_name, url_args, url_kwargs: user.is_staff,
            # }
        ]
    },
]


OSCAR_ALLOW_ANON_CHECKOUT = True

# Brand settings
OSCAR_SHOP_NAME = 'Rugeast'
OSCAR_SHOP_TAGLINE = ""
# OSCAR_HOMEPAGE = reverse_lazy('catalogue:index')
OSCAR_HOMEPAGE = reverse_lazy('home')
OSCAR_ACCOUNTS_REDIRECT_URL = 'customer:profile-view'
OSCAR_RECENTLY_VIEWED_PRODUCTS = 20
OSCAR_RECENTLY_VIEWED_COOKIE_LIFETIME = 604800  # one week
OSCAR_RECENTLY_VIEWED_COOKIE_NAME = 'teemche_history'
OSCAR_HIDDEN_FEATURES = []

# Communication settings
OSCAR_EAGER_ALERTS = True
OSCAR_SEND_REGISTRATION_EMAIL = False
OSCAR_SEND_PLACED_ORDER = False
OSCAR_FROM_EMAIL = 'hi@takwin.io'
OSCAR_STATIC_BASE_URL = None
OSCAR_SAVE_SENT_EMAILS_TO_DB = True

# Tax
# OSCAR_OFFER_ROUNDING_FUNCTION = decimal.Decimal.quantize
OSCAR_OFFERS_INCL_TAX = False


# Currency
OSCAR_DEFAULT_CURRENCY = 'EUR'
OSCAR_CURRENCY_LOCALE = 'EUR'
OSCAR_CURRENCY_FORMAT = {
    'EUR': {
        # 'format': '#,##0\xa0',
        # 'format': '#,##0 €',
    }
}

# OSCAR Pagination
OSCAR_PRODUCTS_PER_PAGE = 20
OSCAR_OFFERS_PER_PAGE = 20
OSCAR_REVIEWS_PER_PAGE = 20
OSCAR_NOTIFICATIONS_PER_PAGE = 20
OSCAR_EMAILS_PER_PAGE = 20
OSCAR_ORDERS_PER_PAGE = 20
OSCAR_ADDRESSES_PER_PAGE = 20
OSCAR_STOCK_ALERTS_PER_PAGE = 20
OSCAR_DASHBOARD_ITEMS_PER_PAGE = 250


OSCAR_SEARCH_FACETS = {
    'fields': OrderedDict([
        ('product_class', {'name': _('Type'), 'field': 'product_class'}),
        ('rating', {'name': _('Rating'), 'field': 'rating'}),
    ]),
    'queries': OrderedDict([
        ('price_range',
         {
             'name': _('Price range'),
             'field': 'price',
             'queries': [
                 # This is a list of (name, query) tuples where the name will
                 # be displayed on the front-end.
                 (_('0 to 20'), '[0 TO 20]'),
                 (_('20 to 40'), '[20 TO 40]'),
                 (_('40 to 60'), '[40 TO 60]'),
                 (_('60+'), '[60 TO *]'),
             ]
         }),
    ]),
}

OSCAR_PRODUCT_SEARCH_HANDLER = 'core.search_handler.CustomProductSearchHandler'

OSCAR_GOOGLE_ANALYTICS_ID = ''

OSCAR_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'line1', 'line4', 'state', 'postcode', 'country', 'phone_number', 'phone_number_fields',)