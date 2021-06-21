from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login',       views.login,            name='login'),
    path('register',    views.register,         name='register'),
    path('logout',      views.logout,           name='logout'),
    path('profile',     views.view_profile,     name='view_profile'),
    path('edit',        views.update_profile,   name='update_profile'),
    path('authors',     views.authors,          name='authors'),
]
