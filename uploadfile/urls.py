from django.urls import path
from rest_framework.routers import DefaultRouter
from uploadfile import views
from django.urls import include

router = DefaultRouter()
router.register(r'upload-file', views.UploadfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
