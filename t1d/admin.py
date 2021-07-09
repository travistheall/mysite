from django.contrib import admin
from .models import (
    Meal,
    Image,
    T1DFood,
    Subject,
    T1DServing
)

admin.site.register(Meal),
admin.site.register(Image),
admin.site.register(Subject),
admin.site.register(T1DFood),
admin.site.register(T1DServing)
