from rest_framework import serializers

from products.models import Product

# product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "sale_price",
            "created_at",
            "updated_at"
        ]
