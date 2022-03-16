from rest_framework import generics, permissions, authentication
from .serializers import ProductSerializer
from .models import Product

# product list view api
# class ProductListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product details view api
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' ?? 


# product create view api and list view api combined
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# update api view
class ProductUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # perform update
    def perform_update(self, serializer):
        # serializer.save(updated_by=self.request.user)
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


# delete api view
class ProductDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'   


# product_list_view_api = ProductListView.as_view()
product_details_view_api = ProductDetailView.as_view()
product_list_create_view_api = ProductListCreateView.as_view()
product_update_view_api = ProductUpdateView.as_view()
product_delete_view_api = ProductDeleteView.as_view()