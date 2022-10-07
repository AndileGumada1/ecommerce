from unittest import skip, TestCase

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from store.models import Category, Product


# @skip("skipping a test")
# class TestSkip(TestCase):
#     def test_skipping(self):
#         pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')

    def test_homepage_url(self):
        """
        Testing home page response
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail(self):
        """
        Testing home page response
        """
        response = self.c.get(reverse('store:product_detail', args=['dango']))
        self.assertEqual(response.status_code, 200)
