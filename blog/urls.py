from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog/<str:slug>/', views.blog_post, name='post_detail'),
    path('blog/category/<category_slug>/', views.post_by_category, name='category'),
    path('search/', views.search, name='search'),



]

