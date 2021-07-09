from rest_framework.viewsets import ModelViewSet
from .models import (
    Subject,
    Meal,
    Image,
    T1DFood,
    T1DServing
)
from .serializers import (
    SubjectSerializer,
    MealSerializer,
    ImageSerializer,
    T1DFoodSerializer,
    T1DServingSerializer
)
from .filters import (
    ImageFilter,
    MealFilter,
    T1DFoodFilter
)
from .pagination import LargeResultsSetPagination


class SubjectView(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    pagination_class = LargeResultsSetPagination


class MealView(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    filterset_class = MealFilter
    pagination_class = LargeResultsSetPagination


class ImageView(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filterset_class = ImageFilter


class T1DFoodView(ModelViewSet):
    queryset = T1DFood.objects.all()
    serializer_class = T1DFoodSerializer
    filterset_class = T1DFoodFilter


class T1DServingView(ModelViewSet):
    queryset = T1DServing.objects.all()
    serializer_class = T1DServingSerializer

