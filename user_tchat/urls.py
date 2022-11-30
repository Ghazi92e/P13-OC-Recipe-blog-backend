from django.urls import path
from rest_framework.routers import DefaultRouter
from user_tchat import views
from django.urls import include

router = DefaultRouter()
router.register(r'user-tchat', views.UserTchatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]