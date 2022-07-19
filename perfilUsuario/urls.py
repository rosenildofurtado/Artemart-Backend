from django.urls import path
from perfilUsuario import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.PerfilPostView.as_view()),
    path('info/', views.PerfilInfoView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('tokensignin/', views.VerifyTokenGoogle.as_view())
]
