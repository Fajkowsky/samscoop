from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import LoginForm, UserForm
from django.contrib.auth import authenticate, login as d_login, logout as d_logout
from django.contrib.auth.models import User
from models import Questions, Answer
import re

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
                return HttpResponse("No such user in database.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    d_logout(request)
    return redirect('login')

@login_required
def index(request):
    return render(request, 'index.html', {'user': request.user})


@login_required
def admin(request):
    if not request.user.is_superuser:
        return HttpResponse('You cant be here!')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User(
                username=cd['username'],
                is_staff=True
            )
            user.set_password(cd['password'])
            user.save()
    else:
        form = UserForm()
    users = User.objects.all().filter(is_superuser=False)
    return render(request, 'admin.html', {'form': form, 'users': users})


@login_required
def survey(request):
    def parser(data):
        p = re.compile(r"\d\.\d\w?")
        w = re.compile("\d\-\d")
        tmp = {}
        for key, value in data.items():
            match = p.match(key)
            if match:
                if not match.group() in tmp:
                    tmp[match.group()] = {
                        'yes_no': '',
                        'ages': []
                    }
                if data[key] == 'on':
                    age = w.search(key)
                    tmp[match.group()]['ages'].append(age.group())
                else:
                    tmp[match.group()]['yes_no'] = data[key]
        print(tmp)
    if request.method == 'POST':
        parser(request.POST)
    questions = Questions.objects.all()
    answers = Answer.objects.all()
    return render(request, 'survey.html', {'questions': questions, 'answers': answers})
