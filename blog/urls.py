from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('search/', views.search_blog, name='search_blog'),
    path('about/', views.about, name='about'),
    path('my-articles/', views.my_articles, name='my_articles'),
    path('my-drafts/', views.my_drafts, name='my_drafts'),
    path('edit-article/<int:blog_id>/', views.edit_article, name='edit_article'),
    path('<slug:slug>/', views.article, name='article'),
    path('<slug:slug>/add_star/', views.add_star, name='add_star'),
]
