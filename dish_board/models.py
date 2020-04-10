from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DishType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, verbose_name='Название')
    ingredients = models.CharField(max_length=400, verbose_name="Ингредиенты")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип блюда'
        verbose_name_plural = 'Типы блюд'
        db_table = 'dish_types'


class Cook(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speed = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name="Кол-во блюд в час")
    preparing_speed = models.DecimalField(default=0, max_digits=5, decimal_places=2,
                                          verbose_name="Скорость подготовки к приготовлению (шт/ч)")
    ingredients_speed = models.DecimalField(default=0, max_digits=5, decimal_places=2,
                                            verbose_name="Скорость наполнения ингредиентами (шт/ч)")
    dish_count = models.IntegerField(default=0, verbose_name="Кол-во блюд на приготовление")

    def update_profile(request, user_id):
        user = User.objects.get(pk=user_id)
        user.save()

    def __unicode__(self):
        return self.user.first_name + self.user.last_name

    def __str__(self):
        return self.user.first_name + self.user.last_name

    class Meta:
        verbose_name = 'Повар'
        verbose_name_plural = 'Повара'
        db_table = 'cooks'
        ordering = ['dish_count']


class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    spiciness = (('t1', 'Не острое'), ('t2', 'Острое'), ('t3', 'Очень острое'))
    dish_spiciness = models.CharField(max_length=2, choices=spiciness, default='t2', verbose_name='Острота')
    portion = (('M', '300-500 г'), ('L', '600-1000 г'))
    dish_portion = models.CharField(max_length=1, choices=portion, default='M', verbose_name='Порция')
    status = (('o', 'Подготовление'), ('i', 'Наполнение ингредиентами'), ('b', 'На готовке'), ('r', 'Готово'))
    status = models.CharField(max_length=1, choices=status, default='o', verbose_name='Статус')
    order_id = models.IntegerField(verbose_name='Номер заказа')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата обновления')
    cook = models.ForeignKey(Cook, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.type.name

    def __str__(self):
        return self.type.name

    def update_status(self):
        update = {'o': 'i',
                  'i': 'b',
                  'b': 'r',
                  'r': 'o'}
        self.status = update[self.status]
        self.save()
        return self

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюдо'
        db_table = 'dishes'
