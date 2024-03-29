"""mstproject1 URL Configuration

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
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.Indexpage,name="index"),
    path('register',views.Signuppage,name="register"),
    path('login',views.Loginpage,name="login"),
    path('logout',views.Logoutpage, name="logout"),
    path('myaccount',views.Myaccount,name="myaccount"),
    path('base', views.base, name= 'base'),
    
    path('admin/', include('msadmin.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
