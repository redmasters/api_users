from django.contrib import admin
from django.urls import path, re_path
from api import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/$', views.api_list),
    re_path(r'^api/api/([0-9])$', views.api_detail)
]