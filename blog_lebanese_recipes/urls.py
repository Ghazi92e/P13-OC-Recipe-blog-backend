"""blog_lebanese_recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog_lebanese_recipes.settings import DEBUG
from blog_lebanese_recipes.settings import MEDIA_URL
from blog_lebanese_recipes.settings import MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('', include('users.urls')),
    path('', include('categories.urls')),
    path('', include('role.urls')),
    path('', include('favoriterecipe.urls')),
    path('', include('like.urls')),
    path('', include('comment.urls')),
    path('', include('uploadfile.urls')),
]

if DEBUG:
  urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
