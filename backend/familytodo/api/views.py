from rest_framework import viewsets
from familytodo.models import *
from .serializers import *


class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class TodolistViewSet(viewsets.ModelViewSet):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()

