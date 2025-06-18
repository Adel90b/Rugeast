import requests
from concurrent.futures import ThreadPoolExecutor
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'cached all of products images'

    def fetch_page(self, page):
        url = f'http://127.0.0.1:80/api/products/?page={page}'
        print(f'send {page}')
        try:
            response = requests.get(url)
            print(f'fetch {page}: {response.status_code}')
        except requests.RequestException as e:
            print(f'Error fetching page {page}: {e}')

    def handle(self, *args, **options):
        pages = 245
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(self.fetch_page, range(1, pages))


# from time import sleep
#
# import requests
# from django.core.management import BaseCommand
#
# class Command(BaseCommand):
#     help = 'cached all of products images'
#
#     def handle(self, *args, **options):
#         pages = 245
#         for page in range(1, pages):
#             url = f'http://127.0.0.1:80/api/products/?page={page}'
#             print(f'send {page}')
#             response = requests.get(url)
#             print(f'send {response.status_code}')
#         #     form = '50001259'
#         #     to = '09381029915'
#         #     username = 'armandavari'
#         #     password = 'A12345678a'
#         #     text = f'{page}'
#         #     url = f'http://tsms.ir/url/tsmshttp.php?from={form}&to={to}&username={username}&password={password}&message={text}'
#         #     if page % 10 == 0:
#         #         requests.get(url)
#         #
#         #     if response.status_code == 200:
#         #         print('check')
#         #         continue
#         #     else:
#         #         print('error')
#         #         sleep(1)
#         #         url = f'http://127.0.0.1:80/api/products/?page={page}'
#         #         response = requests.get(url)
#         #         continue