from django.urls import path

from . import views

urlpatterns = [
    path('get-titles/', views.get_titles, name='get_titles')
]
