from rest_framework import routers
from .api import ProductViewSet

router=routers.DefaultRouter()
router.register('products',ProductViewSet,'products')

urlpatterns=router.urls