from rest_framework import serializers

from backend.products.models import Product

# product serializer
class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'pk'
            'name',
            'description',
            'price',
            'sale_price'
            'discount'
            'created_at',
            'updated_at'
        ]

    def get_discount(self, obj):
        return obj.get_discount()
