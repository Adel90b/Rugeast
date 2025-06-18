from django.conf import settings
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from apps.offer.models import Range
from oscar.apps.search.forms import BrowseCategoryForm
from oscar.core.loading import get_model, get_class

Product = get_model('catalogue', "Product")
SimpleProductSearchHandler = get_class('catalogue.search_handlers', 'SimpleProductSearchHandler')


class CustomProductSearchHandler(SimpleProductSearchHandler):
    form_class = BrowseCategoryForm
    model_whitelist = [Product]
    paginate_by = settings.OSCAR_PRODUCTS_PER_PAGE
    SORT_FIELDS = {
        'max_price': '-stockrecords__price',
        'min_price': 'stockrecords__price',
        'date_newest': '-date_created',
        'offer': 'offer',
        # 'date_latest': 'date_created',
    }

    def check_string(self, input_str):
        if len(input_str) == 3:
            return input_str
        elif len(input_str) == 2:
            return '0'+input_str
        elif len(input_str) == 1:
            return '00' + input_str
        else:
            return input_str

    def get_search_context_data(self, context_object_name):
        self.context_object_name = context_object_name
        context = self.get_context_data(object_list=self.object_list)
        context[context_object_name] = context['page_obj'].object_list
        return context

    def __init__(self, request_data, full_path, categories=None):
        self.request_data = request_data
        super().__init__(request_data, full_path, categories)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(number_in_stock=Sum('stockrecords__num_in_stock'))
        qs = qs.order_by('-number_in_stock')
        # qs = qs.order_by('?')
        query_name = self.request_data.get('q', None)
        range_slug = self.request_data.get('range', None)

        if range_slug:
            range = get_object_or_404(Range, slug=range_slug, is_public=True)
            qs = range.all_products()
            qs = qs.order_by('rangeproduct__display_order')

        if query_name:
            search_vector = SearchVector('title', weight='A') + SearchVector('dc', weight='B')\
                            + SearchVector('slug', weight='C') + SearchVector('description', weight='D')
            search_query = SearchQuery(query_name)
            # qs = qs.annotate(search=search_vector, rank=SearchRank(search_vector, search_query))\
            #     .filter(search=search_query).order_by("-rank")
            qs = qs.annotate(search=search_vector).filter(search=search_query)

        if self.categories:
            qs = qs.filter(categories__in=self.categories).distinct()

        if self.request_data:
            qs = self.filter_by_attribute(self.request_data, qs)

        return qs

    def filter_by_attribute(self, data, products):
        color = data.get('colors', None)
        category = data.get('categories', None)
        min_width = data.get('startWide', None)
        max_width = data.get('endWide', None)


        sort_field = data.get('sortType', None)
        if sort_field == "random":
            products = products.all().order_by('?')
        if sort_field and sort_field == "offer":
            all_products = products.all()
            products_list = []
            for product in all_products:
                if product.has_offer():
                    products_list.append(product)
            products = products_list

        elif sort_field and sort_field in self.SORT_FIELDS:
            sort_type = self.SORT_FIELDS[sort_field]
            products = products.filter().order_by(sort_type)

        if min_width == '0' and max_width == '100':
            min_width = None
            max_width = None

        min_length = data.get('startLength', None)
        max_length = data.get('endLength', None)
        if min_length == '0' and max_length == '100':
            min_length = None
            max_length = None



        if category is not None:
            category = str(category).replace('dorf','2').replace('preserteppice','1').replace('modernTappiche','4').replace('AntikeCategory','5').replace('pakistanAfghan','3').split(',')
            # category = str(category).split(',')
            products = products.filter(categories__in=category)


        long = data.get('long', None)
        if long:
            products = products.filter_by_attributes(long=self.check_string(long))

        width = data.get('width', None)
        if width:
            products = products.filter_by_attributes(width=self.check_string(width))

        price = data.get('price', None)
        if price:
            products = products.filter(stockrecords__price_excl_tax=price)

        max_price = data.get('endPrice', None)
        if max_price:
            products = products.filter(stockrecords__price_excl_tax__lte=max_price)

        min_price = data.get('startPrice', None)
        if min_price:
            products = products.filter(stockrecords__price_excl_tax__gte=min_price)

        if min_width:
            products = products.filter_by_attributes(width__gte=self.check_string(min_width))
            # products = [pr for pr in products if
            #             hasattr(pr.attr, 'width') and int(str(pr.attr.width)) >= int(min_width)]

        if max_width:
            products = products.filter_by_attributes(width__lte=self.check_string(max_width))
            # products = [pr for pr in products if
            #             hasattr(pr.attr, 'width') and int(str(pr.attr.width)) <= int(max_width)]

        if min_length:
            products = products.filter_by_attributes(length__gte=self.check_string(min_length))
            # products = [pr for pr in products if
            #             hasattr(pr.attr, 'length') and int(str(pr.attr.length)) >= int(min_length)]

        if max_length:
            products = products.filter_by_attributes(length__lte=self.check_string(max_length))
            # products = [pr for pr in products if
            #             hasattr(pr.attr, 'length') and int(str(pr.attr.length)) >= int(min_length)]

        if color is not None:
            try:
                colors = str(color).split(',')
                COLOR_CODES = {
                    'brown': 'Brown / Yellow', 'green': 'Green  / Olive', 'blue': 'Blue / Turquoise', 'violet': 'Purple / Pink',
                    'gray': 'Black / Gray',
                    'cream': 'White / Cream', 'red': 'Red / Orange', 'multiColor': 'Multicolor',
                }
                colors = [COLOR_CODES[color] for color in colors]
                # 'brown,blue,red,violet,green,gray,multiColor,cream'
                # products = [pr for pr in products if
                #             hasattr(pr.attr, 'color') and str(pr.attr.color) in colors]
                products = products.filter_by_attributes(color__in=colors)
            except:
                pass

        shape = data.get('shapes', None)
        if shape is not None:
            shapes = str(shape).replace('vertRect','Runner').replace('square','Square').replace('circle','Round').replace('horRect','Rectangle').replace('oval','Oval').split(',')

            # products = [pr for pr in products if
            #             hasattr(pr.attr, 'form') and str(pr.attr.form) in shapes]
            products = products.filter_by_attributes(form__in=shapes)

        return products