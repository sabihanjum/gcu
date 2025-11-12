from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('', views.author_list, name='list'),
    path('add/', views.author_add, name='add'),
    path('<int:id>/edit/', views.author_edit, name='edit'),
    path('<int:id>/delete/', views.author_delete, name='delete'),
]