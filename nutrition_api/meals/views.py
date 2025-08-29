from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MealSerializer
from rest_framework import viewsets, filters
from .models import Meal
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
        return qs
