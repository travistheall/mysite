from .models import Subject, Meal, Image, T1DFood, T1DServing
# from fndds.serializers import FoodSerializer
from rest_framework.serializers import HyperlinkedModelSerializer


class SubjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class MealSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class ImageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class T1DFoodSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = T1DFood
        fields = '__all__'


class T1DServingSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = T1DServing
        fields = '__all__'
