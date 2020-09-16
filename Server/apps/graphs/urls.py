from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from graphs import views


# Create a router and register our viewsets with it.
from graphs.views import GraphViewSet

router = DefaultRouter()
router.register(r'results', views.ResultViewSet, basename='results')
# router.register(r'graphManage', views.GraphViewSet, basename="Graph")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('graphManage/', GraphViewSet.as_view()),

]