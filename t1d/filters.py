from django.db import models
from django_filters import CharFilter, DateTimeFilter
import datetime
from django_filters import rest_framework as filters
import django_filters
from .models import (
    Meal,
    Image,
    T1DFood,
)


class MealFilter(filters.FilterSet):
    class Meta:
        model = Meal
        fields = ['subjectid', 'date', 'name']


class ImageFilter(filters.FilterSet):
    class Meta:
        model = Image
        fields = ['mealid', 'id']


class T1DFoodFilter(filters.FilterSet):
    class Meta:
        model = T1DFood
        fields = ['meal']
