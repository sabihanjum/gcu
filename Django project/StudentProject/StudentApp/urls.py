from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('addcourse/', views.addcourse, name='addcourse'),
]