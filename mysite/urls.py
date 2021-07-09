import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from fndds.views import (
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

from t1d.views import (
    T1DFoodView,
    SubjectView,
    MealView,
    ImageView,
    T1DServingView
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


router.register('t1d_food', T1DFoodView)
router.register('subject', SubjectView)
router.register('meal', MealView)
router.register('images', ImageView)
router.register('servings', T1DServingView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('__debug__/', include(debug_toolbar.urls)),
]
