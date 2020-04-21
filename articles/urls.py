
from django.urls import path
from .import views
from django.conf.urls import include, url

app_name = 'articles'

urlpatterns = [

    path('',views.article_list, name="list"),
    path('one', views.article_one, name = "one"),
    path('create', views.article_create, name="create"),
    path('<slug:slug>/', views.article_detail, name="detail"),


]
