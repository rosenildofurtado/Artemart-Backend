from django import urls
from fazerbusca.views import ArteViewSet
from rest_framework.routers import DefaultRouter





router = DefaultRouter()
router.register(r'arte',ArteViewSet)
urlpatterns = router.urls
