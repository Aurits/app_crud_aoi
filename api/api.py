from .models import Product
from rest_framework import viewsets,permissions
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class=ProductSerializer

    def get_queryset(self):
        return self.request.user.products.all()
    
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

    