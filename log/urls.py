from log import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'',views.LogViewSet)
urlpatterns = router.urls