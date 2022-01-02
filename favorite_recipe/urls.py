from django.urls import path
from rest_framework.routers import DefaultRouter
from favorite_recipe import views
from django.urls import include

router = DefaultRouter()
router.register(r'api-favorite_recipe', views.FavoriteRecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]