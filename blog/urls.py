from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blog_id>/', views.article, name='article'),
    path('<int:blog_id>/add_star/', views.add_star, name='add_star')
]
