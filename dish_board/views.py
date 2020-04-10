from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from dish_board.forms import UserForm, CookForm, DishForm
from .models import Cook, Dish


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = CookForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!'))
            return redirect('settings:profile')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = CookForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def dish_board_work(request):
    name = 'Hello, ' + request.user.get_full_name()
    queryset = Dish.objects.filter(cook__user=request.user)
    l = list(queryset)
    context = {
        'name': name,
        'queryset': l
    }
    return render(request, 'dish_board_work.html', context)


def dish_order(request):
    queryset_cook = Cook.objects.order_by('dish_count').filter(user__is_active=True).first()
    form = DishForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.cook = queryset_cook;
        instance.save()
        queryset_cook.dish_count += 1
        queryset_cook.save()
        messages.success(request, 'Ok')
    else:
        messages.error(request, 'Something is wrong')
    context = {
        'form': form
    }
    return render(request, 'dish_order_create.html', context)
