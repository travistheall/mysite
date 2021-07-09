from django.contrib import admin
from .models import (Food,
                     Portion,
                     Nutrient,
                     Subcode,
                     Derivation,
                     Ingredient,
                     Moisture,
                     NutrientValue,
                     Weight)

admin.site.register(Portion),
admin.site.register(Nutrient),
admin.site.register(Subcode),
admin.site.register(Food),
admin.site.register(Derivation),
admin.site.register(Ingredient),
admin.site.register(Moisture),
admin.site.register(NutrientValue),
admin.site.register(Weight),