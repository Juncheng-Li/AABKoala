import os

from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from apps.graphs.Services import graphService
from apps.graphs.models import Result, Graph, Nds_3dcrt
from apps.graphs.serializers import ResultSerializer, UserSerializer, GraphSerializer


class ResultViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResultListViewSet(APIView):
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @swagger_auto_schema(operation_description="insert list of results. \n [{Result1},{Result2}...]",
                         request_body=ResultSerializer(many=True))
    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = ResultSerializer(data=request.data, many=True)
        else:
            serializer = ResultSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GraphViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(operation_description="get all graphs information",
                         responses={200: openapi.Response('list of all graphs information', GraphSerializer)})
    def get(self, request):
        graphs = Graph.objects.all()
        serializer = GraphSerializer(graphs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="plot graph",
     request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'graphType': openapi.Schema(type=openapi.TYPE_STRING, description="Type of ploting graph"),
            'mode': openapi.Schema(type=openapi.TYPE_STRING, description="Mode of ploting graph"),
            'facilitys': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                '{FacilityName}': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.TYPE_INTEGER,
                                                 description='resultids (example: [99, 101])'),
            }),
        }
    ))
    def post(self, request):
        graphType = json.loads(request.body.decode('utf-8')).get('graphType')
        if graphType == "NDS_3DCRT":
            return graphService.plot_NDS_3DCRT(self, request)
        elif graphType == "NDS_IMRT":
            return graphService.plot_NDS_IMRT(self, request)

    @swagger_auto_schema(operation_description="delete graph according ids ",
     request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'graphs_list': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.TYPE_INTEGER,
                                          description='resultids (example: [99, 101])')
        }
    ))
    def delete(self, request):
        graphs_list = json.loads(request.body.decode('utf-8')).get('graphs_list')

        graphs_obj = Graph.objects.filter(pk__in=graphs_list)
        for graph_obj in graphs_obj:
            url = graph_obj.url
            os.remove(url)
            graph_obj.result.clear()
            graph_obj.delete()

        return Response(status=status.HTTP_200_OK)
