from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('update-daily/', csrf_exempt(views.update_daily), name='update_daily'),
]
