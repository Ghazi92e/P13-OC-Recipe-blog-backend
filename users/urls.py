from django.db import router
from django.urls import path, include
from users import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'api-users', views.UserViewSet)

urlpatterns = [
    # path('api-users/', views.users_list),
    # path('api-recipes/<int:pk>/', views.recipes_detail),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]