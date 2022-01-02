from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from role import views

router = DefaultRouter()
router.register(r'api-role', views.RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]