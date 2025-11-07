from django.urls import path
from . import views

app_name = 'bride'

urlpatterns = [
    path('', views.home, name='home'),
]