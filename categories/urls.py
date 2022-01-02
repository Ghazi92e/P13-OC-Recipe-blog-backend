from rest_framework.routers import DefaultRouter
from categories import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'api-categories', views.CategoriesViewSet)

urlpatterns = [

    path('', include(router.urls)),
]