from .models import (Food,
                     Portion,
                     Nutrient,
                     Subcode,
                     Derivation,
                     Ingredient,
                     Moisture,
                     NutrientValue,
                     Weight)
from rest_framework.serializers import HyperlinkedModelSerializer


class FoodSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class PortionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Portion
        fields = '__all__'


class NutrientSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Nutrient
        fields = '__all__'


class SubcodeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Subcode
        fields = '__all__'


class DerivationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Derivation
        fields = '__all__'


class IngredientSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class MoistureSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Moisture
        fields = '__all__'


class NutrientValueSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = NutrientValue
        fields = '__all__'


class WeightSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'


#TODO: Do This For Others
class ListWeightSerializer(WeightSerializer):
    food = FoodSerializer(many=False)
    subcode = SubcodeSerializer(many=False)
    portion = PortionSerializer(many=False)

    def to_representation(self, instance):
        new = FoodSerializer(instance)
        new['desc']

    class Meta:
        model = Weight
        fields = ['food', 'subcode', 'portion', 'value']