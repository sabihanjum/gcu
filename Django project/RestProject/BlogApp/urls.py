from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

route = DefaultRouter()
route.register(r'blogs', BlogViewSet, basename='blog')

urlpatterns = [
    path('api/', include(route.urls)),
]
