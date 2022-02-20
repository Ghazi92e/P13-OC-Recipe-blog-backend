from django.urls import path
from rest_framework.routers import DefaultRouter
from relationships import views
from django.urls import include

router = DefaultRouter()
router.register(r'api-relationships', views.RelationshipsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]