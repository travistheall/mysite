from rest_framework.viewsets import ModelViewSet
from .models import (Food,
                     Portion,
                     Nutrient,
                     Subcode,
                     Derivation,
                     Ingredient,
                     Moisture,
                     NutrientValue,
                     Weight)
from .serializers import (FoodSerializer,
                          PortionSerializer,
                          NutrientSerializer,
                          SubcodeSerializer,
                          DerivationSerializer,
                          IngredientSerializer,
                          MoistureSerializer,
                          NutrientValueSerializer,
                          WeightSerializer, ListWeightSerializer)
from .filters import FoodFilter, WeightFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers


class FoodView(ModelViewSet):
    queryset = Food.objects.all().prefetch_related('ingredients')
    serializer_class = FoodSerializer
    filterset_class = FoodFilter


class PortionView(ModelViewSet):
    queryset = Portion.objects.all()
    serializer_class = PortionSerializer


class NutrientView(ModelViewSet):
    queryset = Nutrient.objects.all()
    serializer_class = NutrientSerializer


class SubcodeView(ModelViewSet):
    queryset = Subcode.objects.all()
    serializer_class = SubcodeSerializer


class DerivationView(ModelViewSet):
    queryset = Derivation.objects.all()
    serializer_class = DerivationSerializer


class IngredientView(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class MoistureView(ModelViewSet):
    queryset = Moisture.objects.all()
    serializer_class = MoistureSerializer


class NutrientValueView(ModelViewSet):
    queryset = NutrientValue.objects.all()
    serializer_class = NutrientValueSerializer


#TODO: Do This For Others
class WeightView(ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    filterset_class = WeightFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ListWeightSerializer
        else:
            return WeightSerializer
