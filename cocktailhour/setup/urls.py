"""cocktailhour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from cocktail import views 
import os
from pathlib import Path
from django.views.generic.base import TemplateView



BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/uploads/'

MEDIA_ROOT= os.path.join(BASE_DIR, 'uploads')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path(r'edit/<cocktail_uid>', views.updateCocktail, name='updateRecipe'),
    # path(r'', views.create, name='create'),
    path(r'', views.get_cocktails, name='cocktails'),
    path('delete/<cocktail_uid>/', views.delete, name='delete'),
    path(r'get/cocktail/<cocktail_uid>', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
       
app_name = "main"   