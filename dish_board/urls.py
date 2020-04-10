from django.conf.urls import url
from .views import(dish_board_work, dish_order)

urlpatterns = [
    url(r'^work/$', dish_board_work),
    url(r'^order/$', dish_order)
]
