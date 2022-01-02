from django.urls import path
from rest_framework.routers import DefaultRouter
from comment import views
from django.urls import include

router = DefaultRouter()
router.register(r'api-comment', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]