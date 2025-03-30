from django.urls import path
from . import views as v
from .views import AddNewProduct, UpdateProduct

app_name = 'products'

urlpatterns = [
    path('', v.index, name='index'),
    path('category/<int:category_id>/', v.category, name='category'),
    # path('search/', SearchResultsView.as_view(), name='search'),
    path('search/', v.search_product, name='search'),
    path('basket/', v.basket, name='basket'),
    path('basket/add/<int:product_id>/', v.basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/',
         v.basket_remove,
         name='basket_remove'),
    path('create_product/', AddNewProduct.as_view(), name='create_product'),
    path('edit_product/<int:pk>',
         UpdateProduct.as_view(),
         name='edit_product'),
    path('delete_product/<int:product_id>',
         v.delete_product,
         name='delete_product'),
]
