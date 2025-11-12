from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_fun, name='login'),
    path('logout/', views.logout_fun, name='logout'),
    path('register/', views.register, name='register'),
    path('book/', include('Book.urls')),
    path('author/', include('AuthorApp.urls')),
]