# Generated by Django 2.2.12 on 2020-04-10 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Кол-во блюд в час')),
                ('preparing_speed', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Скорость подготовки к приготовлению (шт/ч)')),
                ('ingredients_speed', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Скорость наполнения ингредиентами (шт/ч)')),
                ('dish_count', models.IntegerField(default=0, verbose_name='Кол-во блюд на приготовление')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['dish_count'],
                'db_table': 'cooks',
                'verbose_name_plural': 'Повара',
                'verbose_name': 'Повар',
            },
        ),
        migrations.CreateModel(
            name='DishType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('ingredients', models.CharField(max_length=400, verbose_name='Ингредиенты')),
            ],
            options={
                'db_table': 'dish_types',
                'verbose_name_plural': 'Типы блюд',
                'verbose_name': 'Тип блюда',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dish_spiciness', models.CharField(choices=[('t1', 'Не острое'), ('t2', 'Острое'), ('t3', 'Очень острое')], default='t2', max_length=2, verbose_name='Острота')),
                ('dish_portion', models.CharField(choices=[('M', '300-500 г'), ('L', '600-1000 г')], default='M', max_length=1, verbose_name='Порция')),
                ('status', models.CharField(choices=[('o', 'Подготовление'), ('i', 'Наполнение ингредиентами'), ('b', 'На готовке'), ('r', 'Готово')], default='o', max_length=1, verbose_name='Статус')),
                ('order_id', models.IntegerField(verbose_name='Номер заказа')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('cook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dish_board.Cook')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dish_board.DishType')),
            ],
            options={
                'db_table': 'dishes',
                'verbose_name_plural': 'Блюдо',
                'verbose_name': 'Блюдо',
            },
        ),
    ]