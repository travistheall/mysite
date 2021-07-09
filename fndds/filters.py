# Django main imports
from django.db import models
# Django Filters imports
from django_filters import rest_framework as filters
from django_filters import CharFilter
# My imports
from .models import Food, Weight


class FoodFilter(filters.FilterSet):
    class Meta:
        model = Food
        fields = ['id',
                  'desc']
        filter_overrides = {
            models.CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }
        }

class WeightFilter(filters.FilterSet):
    class Meta:
        model = Weight
        fields = ['food', 'portion']
