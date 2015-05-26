from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'login.html')

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
