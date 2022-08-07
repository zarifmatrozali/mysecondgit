"""forward URL Configuration

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
from django.urls import path
from django.urls import re_path,include
from hello_world import views
from forward.settings import DEBUG, STATIC_URL, STATIC_DIR, MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.index,name='index'),
    re_path(r'^special/',views.special,name='special'),
    re_path(r'^hello_world/',include('hello_world.urls')),
    # re_path(r'^combine/',include('combine.urls')),
    # re_path(r'^book/',include('book.urls')),
    re_path(r'^logout/$',views.user_logout, name='logout')
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)