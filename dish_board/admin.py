from django.contrib import admin

from .models import DishType
from .models import Cook
from .models import Dish


class DishTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'ingredients']

    class Meta:
        model = DishType


class CookAdmin(admin.ModelAdmin):
    list_display = ['user', 'speed', 'preparing_speed',
                    'ingredients_speed', 'dish_count']

    class Meta:
        model = Cook


class DishAdmin(admin.ModelAdmin):
    list_display = ['type', 'dish_spiciness', 'dish_portion', 'status',
                    'order_id', 'cook', 'timestamp', 'updated']

    class Meta:
        model = Dish


admin.site.register(DishType, DishTypeAdmin)
admin.site.register(Cook, CookAdmin)
admin.site.register(Dish, DishAdmin)
