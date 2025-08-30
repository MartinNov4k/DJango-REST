from rest_framework import serializers
from .models import Meal

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ["id", "user","created_at", "calories", "protein_g", "carbs_g", "fat_g", "sugar_g", "name"]
        read_only_fields = ["id", "created_at"]
