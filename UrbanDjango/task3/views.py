from django.shortcuts import render


def get_platform(request):
    return render(request, 'third_task/platform.html')


# Create your views here.

def get_games(request):
    atom = 'Atomic Heart'
    cyber = 'Cyberpunk 2077'
    pay = 'PayDay 2'
    context = {'atom': atom, 'cyber': cyber, 'pay': pay}
    return render(request, 'third_task/games.html', context)


def get_cart(request):
    return render(request, 'third_task/cart.html')
