from django.urls import path
from rest_framework.routers import DefaultRouter
from recipes import views
from django.urls import include

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)

urlpatterns = [

    path('', include(router.urls)),

    # path('api-recipes/', views.recipes_list),
    # path('api-recipes/<int:pk>/', views.recipes_detail),
]
