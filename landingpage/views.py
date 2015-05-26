from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import LoginForm
from django.contrib.auth import authenticate, login as d_login


def login(request):
    if request.user.is_authenticated():
        return redirect('index')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['login'],
                password=cd['password']
            )
            if user is not None:
                d_login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def admin(request):
    if not request.user.is_superuser:
        return HttpResponse('You cant be here!')
    return render(request, 'admin.html')


@login_required
def survey(request):
    return render(request, 'survey.html')
