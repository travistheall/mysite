from django.urls import path, include
from rest_framework import routers
from .views import (
    FoodView,
    PortionView,
    NutrientView,
    SubcodeView,
    DerivationView,
    IngredientView,
    MoistureView,
    NutrientValueView,
    WeightView,
)
router = routers.DefaultRouter()
router.register('food', FoodView)
router.register('portion', PortionView)
router.register('nutrient', NutrientView)
router.register('subcode', SubcodeView)
router.register('derivation', DerivationView)
router.register('ingredient', IngredientView)
router.register('moisture', MoistureView)
router.register('nutrientvalue', NutrientValueView)
router.register('weight', WeightView)


urlpatterns = [
    path('fndds/', include(router.urls)),
]