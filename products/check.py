from products.models import Product

print(Product.objects.all())
print(Product.objects.filter(id=1))
