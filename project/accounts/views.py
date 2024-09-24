from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import CustomUser


def index(request):
    return render(request, 'index.html')


def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    new_user = CustomUser(username=username, password=password)
    new_user.save()
    return HttpResponse('ユーザーの作成に成功しました')

