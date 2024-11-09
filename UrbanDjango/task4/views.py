from django.shortcuts import render


def get_platform(request):
    if request.method:
        return render(request, 'fourth_task/platform.html')


# Create your views here.

def get_games(request):
    atom = 'Atomic Heart'
    cyber = 'Cyberpunk 2077'
    pay = 'PayDay 2'
    context = {'games': [atom,cyber, pay]}
    return render(request, 'fourth_task/games.html', context)


def get_cart(request):
    return render(request, 'fourth_task/cart.html')

