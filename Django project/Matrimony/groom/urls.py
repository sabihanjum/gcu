from django.urls import path
# from . import views
from groom import views
app_name = 'groom'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('display/', views.display, name='display'),
    
]
