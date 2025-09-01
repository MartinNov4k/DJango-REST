from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MealSerializer, TargetsSerializer
from rest_framework import viewsets, filters
from .models import Meal, Targets
import json
import os

# Create your views here.

class MealViewSet(viewsets.ModelViewSet):   
    serializer_class = MealSerializer

    def get_queryset(self):
        qs = Meal.objects.all().order_by("-created_at")
        user = self.request.query_params.get("user")
        if user:
            qs = qs.filter(user__iexact=user)

        day = self.request.query_params.get("day")
        if day:
            qs = qs.filter(created_at__date=day)
            
        return qs

class TargetViewSet(viewsets.ModelViewSet):   
    serializer_class = TargetsSerializer

    def get_queryset(self):
        qs = Targets.objects.all()
        user = self.request.query_params.get("user")
        if user:
            qs = qs.filter(user__iexact=user) 
            
        return qs
