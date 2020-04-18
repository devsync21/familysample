from rest_framework import serializers
from familytodo.models import *


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = '__all__'
