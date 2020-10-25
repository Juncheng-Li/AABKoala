from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
from apps.graphs import views
from apps.graphs.views import GraphViewSet, ResultListViewSet

router = DefaultRouter()
router.register(r'results', views.ResultViewSet, basename='results')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('graphManage/', GraphViewSet.as_view(), name='graph_manage'),
    path('resultsList/', ResultListViewSet.as_view(), name='results_list'),

]