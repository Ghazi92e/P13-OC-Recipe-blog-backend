from django.urls import path
from rest_framework.routers import DefaultRouter
from favoriterecipe import views
from django.urls import include

router = DefaultRouter()
router.register(r'favoriterecipe', views.FavoriteRecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]