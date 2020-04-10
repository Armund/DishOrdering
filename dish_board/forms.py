from django import forms
from django.contrib.auth.models import User
from .models import Cook, Dish


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ('speed', 'preparing_speed', 'ingredients_speed')


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['type', 'dish_spiciness', 'dish_portion', 'order_id']
