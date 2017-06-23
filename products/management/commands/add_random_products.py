from django.core.management.base import BaseCommand

from products.models import Product
from random import randint, choice
from string import printable, ascii_uppercase

class Command(BaseCommand):
    def handle(self, *args, **options):

        for i in range(20):
            rand_string = printable
            super_rand_string = ""
            rand_title = '{}{}{}'.format(ascii_uppercase[randint(0, len(ascii_uppercase)-1)],
                                             '-',
                                             randint(1, 5000))
            rand_available = [True, False]
            rand_classification = choice(['flatiron', 'fridge', 'vacuum_cleaner'])
            rand_vacuum_cleaner = ['product/0bd4b6d4-e97f-4b81-8a71-6d75f71a31c3.jpg',
                                   'product/1ff90290-eb9b-4f9a-8fa7-5a74345c30aa.jpg',
                                   'product/9a669519-ad3a-43c1-9f08-fd8f56fbf704.jpg']
            rand_flatiron = ['product/ad22e1e9-4c3e-4172-a82c-b48dcb7f43ac.jpg',
                             'product/d1f1fd54-75d5-45c3-96eb-fe9420cb09b8.jpg']
            rand_fridge = ['product/5c04a4d4-53c5-4539-aeba-c7188585e7ed.jpg',
                           'product/4578480f-2603-4425-a28c-ec7e63a894a5.jpg']

            def rand_img(classification):
                if classification == 'flatiron':
                    image = choice(rand_flatiron)
                elif classification == 'fridge':
                    image = choice(rand_fridge)
                elif classification == 'vacuum_cleaner':
                    image = choice(rand_vacuum_cleaner)
                return image

            for index in range(randint(1, 9)):
                super_rand_string += rand_string[randint(0, len(rand_string) - 1)] * randint(0, 20)

            Product.objects.create(title=rand_title,
                                   description=(super_rand_string + "\n")*randint(0, 5),
                                   price=randint(50, 6000),
                                   available=choice(rand_available),
                                   classification=rand_classification,
                                   image=rand_img(rand_classification))

