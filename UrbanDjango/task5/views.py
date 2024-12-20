from django.shortcuts import render
from .UserRegister import UserForm


# Create your views here.

def sign_up_by_django(request):
    if 'users' not in request.session:
        request.session['users'] = ['user1', 'user2', 'user3']

    users = request.session['users']
    info = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and age >= 18 and username not in users:
                users.append(username)
                request.session['users'] = users
                info['message'] = f"Приветствуем, {username}"
                form = UserForm()

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
        info['form'] = form
    else:
        form = UserForm()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):

    if 'users' not in request.session:
        request.session['users'] = ['user1', 'user2', 'user3']

    users = request.session['users']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        info['username'] = username
        info['password'] = password
        info['repeat_password'] = repeat_password
        info['age'] = age
        if password == repeat_password and int(age) >= 18 and username not in users:
            users.append(username)
            request.session['users'] = users
            info['message'] = f"Приветствуем, {username}"
            info['username'] = ''
            info['password'] = ''
            info['repeat_password'] = ''
            info['age'] = ''
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'

    return render(request, 'fifth_task/registration_page.html', info)
