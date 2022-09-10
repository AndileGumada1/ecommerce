from store.models import Category, Product
from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestCategoriesModel(TestCase):

    # initial setup
    def setUp(self):
        self.data1 = Category.objects.create(name='django',slug='django')

    def test_category_model_entry(self):
        """
        Tests the insertion of data into the Category table
        """
        data = self.data1
        self.assertTrue(isinstance(data,Category))
        
class TestProductsModel(TestCase):
    # initial setup
    def setUp(self):
        self.data1 = Category.objects.create(name='django',slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create()
