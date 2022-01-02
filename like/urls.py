from django.urls import path
from rest_framework.routers import DefaultRouter
from like import views
from django.urls import include

router = DefaultRouter()
router.register(r'api-like', views.LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]