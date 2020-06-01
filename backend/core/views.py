from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from core.models import *
from core.serializers import TitleSerializer


class MyPagination(PageNumberPagination):
    page_size = 15


class TitlesViewSet(ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    pagination_class = MyPagination


