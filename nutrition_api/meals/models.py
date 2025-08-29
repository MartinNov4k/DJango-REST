from django.db import models
from rest_framework import serializers

# Create your models here.
class Meal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.TextField(blank=True)
    calories = models.FloatField(default=0)
    protein_g = models.FloatField(default=0)
    carbs_g = models.FloatField(default=0)
    fat_g = models.FloatField(default=0)
    sugar_g = models.FloatField(default=0)

       
    def __str__(self):
        return f"Meal {self.id} ({self.user})"    