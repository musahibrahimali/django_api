from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

# get all products
@api_view(['GET'])
def products(request):
    '''
        api endpoint for getting all available products
        in the database related to the products model
    '''
    instance = Product.objects.all()
    if instance:
        serializer = ProductSerializer(instance, many=True)
        return Response(serializer.data)
    return Response({'message': 'No products found'})


# get product by id
@api_view(['GET'])
def productById(request, id):
    data = Product.objects.get(pk=id)
    if data:
        serializer = ProductSerializer(data)
        return Response(serializer.data)
    return Response({'message': 'No data found'})


# create product
@api_view(['POST'])
def product(request):
    data = request.data 
    if data:
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    return Response({'message': 'Data supplied is invalid'})
