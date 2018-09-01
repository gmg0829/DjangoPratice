"""DjangoPratice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from article.views import home
from article.views import detail
from article.views import archives
from article.views import about_me
from article.views import search_tag
from article.views import blog_search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^archives/$', archives, name='archives'),
    url(r'^aboutme/$', about_me, name='about_me'),
    url(r'^tag(?P<tag>\w+)/$', search_tag, name='search_tag'),
    url(r'^search/$',blog_search, name = 'search'),
]
