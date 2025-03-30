from django.test import TestCase
from django.db.models import Q
from django.urls import reverse
from products.models import Product, Basket, ProductCategory
from django.core.paginator import Paginator


class IndexTestCase(TestCase):
    fixtures = ['fixtures/products.json', 'fixtures/productcategory.json']

    def test_view(self):
        path = reverse('products:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'Главная страница')
        self.assertTemplateUsed(response, 'products/index.html')

    def test_product(self):
        products = Product.objects.get(id=1)
        name = products.name
        self.assertEqual('Кеды', name)

    def test_pages(self):
        all_products_category = Product.objects.all()
        paginator = Paginator(all_products_category, 3)
        page_obj = paginator.get_page(paginator)
        path = reverse('products:index')
        response = self.client.get(path)
        self.assertEqual(response.context['page_obj'][0], page_obj[0])


class TestCategories(TestCase):

    def test_category(self):
        categories = ProductCategory.objects.get(id=1)
        name = categories.name
        self.assertEqual('Еда', name)


class TestSearch(TestCase):
    fixtures = ['fixtures/products.json', 'fixtures/productcategory.json']

    def test_view(self):
        path = reverse('products:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'Главная страница')
        self.assertTemplateUsed(response, 'products/index.html')

    def test_product(self):
        query = 'Бананы'
        products = Product.objects.get(Q(name__icontains=query))
        self.assertEqual(products.name, 'Бананы')
