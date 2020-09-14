from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from graphs import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'results', views.ResultViewSet)
router.register(r'graphs', views.GraphViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]