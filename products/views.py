from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.core.paginator import Paginator
from products.models import Product, Basket, ProductCategory
from django.contrib.auth import get_user_model
from django.db.models import Q
from products.forms import AddProductForm, EditProductForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


User = get_user_model()


def index(request):
    all_categories = ProductCategory.objects.all()
    all_products = Product.objects.order_by('id')
    paginator = Paginator(all_products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,
                  'products/index.html',
                  context={'categories': all_categories,
                           'page_obj': page_obj,
                           'title': 'Главная страница'})


def category(request, category_id):
    all_categories = ProductCategory.objects.all()
    all_products_category = Product.objects.filter(category_id=category_id)
    paginator = Paginator(all_products_category, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,
                  'products/category.html',
                  context={'categories': all_categories,
                           'page_obj': page_obj})


def search_product(request):
    categories = ProductCategory.objects.all()
    query = request.GET.get('q')
    object_list = Product.objects.filter(Q(name__icontains=query))
    return render(request,
                  'products/index.html',
                  context={'object_list': object_list,
                           'categories': categories})

# class SearchResultsView(ListView):
#     model = Product
#     template_name = 'products/index.html'
#     title = 'Поиск'

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         categories = ProductCategory.objects.all()
#         object_list = Product.objects.filter(Q(name__icontains=query))
#         return object_list, categories


@login_required
def basket(request):
    products = Basket.objects.filter(user=request.user)
    return render(request,
                  'products/basket.html',
                  context={'products_in_basket': products,
                           'title': 'Корзина'})


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user,
                                    product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user,
                              product=product,
                              quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    baskets = Basket.objects.filter(id=basket_id,
                                    user=request.user)
    baskets.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class AddNewProduct(LoginRequiredMixin, CreateView):
    model = Product
    form_class = AddProductForm
    template_name = 'products/add_product.html'
    success_url = reverse_lazy('products:index')


class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = EditProductForm
    template_name = 'products/edit_product.html'
    success_url = reverse_lazy('products:index')


# @login_required
# def create_product(request):
#     form = AddProductForm(request.POST or None, request.FILES)
#     context = {'form': form}
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         return redirect('products:index')
#     return render(request, 'products/add_product.html', context)


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product,
                                id=product_id)
    product.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def error404(request, exception):
    return render(request,
                  'errors/404.html',
                  status=404)


def error403(request, reason=''):
    return render(request,
                  'errors/403.html',
                  status=403)


def error500(request):
    return render(request,
                  'errors/500.html',
                  status=500)
