from publicararte import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'arte',views.ArteViewSet)
router.register(r'tags',views.TagsViewSet)
router.register(r'tematica',views.TematicaViewSet)
router.register(r'categoria',views.CategoriaViewSet)
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]+router.urls
