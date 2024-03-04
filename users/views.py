from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from products.models import Basket

from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()

    data = {
        'form': form,
    }
    return render(request, 'users/login.html', data)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестировались!')
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    form = UserRegistrationForm()
    data = {'form': form}
    return render(request, 'users/registration.html', data)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,
                               data=request.POST,
                               files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)
    # total_sum = 0
    # total_quantity = 0
    # for basket in baskets:
    #     total_sum = total_sum + basket.sum()
    #     total_quantity = total_quantity + basket.quantity

    data = {
        'title': 'UMStore - Профиль',
        'form': form,
        'baskets': baskets,
    }
    return render(request, 'users/profile.html', data)


def logout(request):
    auth.logout(request)
    return redirect('index')
