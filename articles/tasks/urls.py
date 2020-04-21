from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about',views.about),
    path('',views.homepage),
    path('naqib', views.naqib),
    path('articles/', include('articles.urls')),
    path('one', include('articles.urls')),

]

urlpatterns += staticfiles_urlpatterns()
