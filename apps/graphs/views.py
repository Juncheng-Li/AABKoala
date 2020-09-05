from django.shortcuts import render
from rest_framework import generics, viewsets
from graphs.models import Result
from graphs.serializers import ResultSerializer


class ResultViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
