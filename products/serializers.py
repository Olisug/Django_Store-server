from rest_framework import serializers
from rest_framework import fields
from products.models import Product, ProductCategory, Basket


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name',
                                            read_only=True,
                                            allow_null=True)

    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'description',
                  'price',
                  'quantity',
                  'image',
                  'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    # product = serializers.SlugRelatedField(slug_field='name',
    #                                        read_only=True,
    #                                        allow_null=True)
    sum = fields.FloatField()
    total_sum = fields.SerializerMethodField()
    total_quantity = fields.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('id',
                  'product',
                  'quantity',
                  'sum',
                  'total_sum',
                  'total_quantity',
                  'created_timestamp')
        read_only_fields = ('created_timestamp',)

    def get_total_sum(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_sum()

    def get_total_quantity(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_quantity()
