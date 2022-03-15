from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

# api home
@api_view(['GET'])
def api_home(request):
    instance = Product.objects.all()
    # if instance
    if instance:
        data = ProductSerializer(instance).data
        return Response(data)
    return Response({'message': 'No data found'})
