from django.urls import path, include
from rest_framework import routers
from .views import (
    T1DFoodView,
    SubjectView,
    MealView,
    ImageView,
    T1DServingView
)

router = routers.DefaultRouter()
router.register('food', T1DFoodView)
router.register('subject', SubjectView)
router.register('meal', MealView)
router.register('servings', T1DServingView)
router.register('ImageView', ImageView)

urlpatterns = [
    path('t1d/', include(router.urls)),
]