from rest_framework import serializers
from products.models import Product

# product serializer
class ProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "content",
            "price",
            "sale_price",
            "discount_price",
            "created_at",
            "updated_at"
        ]

    def get_discount_price(self, obj):
        return obj.get_discount()
