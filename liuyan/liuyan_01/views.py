from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from liuyan_01 import models
from django.http import HttpResponse

# Create your views here.


def index(request):
    # lname = models.CharField(max_length=1000)
    # lemil = models.CharField(max_length=1000)
    # laddrees = models.CharField(max_length=1000)
    # ltext = models.TextField()


    list = models.liuyan.objects.all()

    return render(request,'liuyan_01/index.html',{'list':list})


def login(request):
    return render(request,'liuyan_01/login.html',{'b':'b'})

# 登录
def login01(request):
    name = request.POST.get("name","")
    pw = request.POST.get("password","")


    try:
        dbname = models.use.objects.get(uname=name)
    except:
            return HttpResponse('账号或密码错误')
    else:
        if name == dbname.uname and pw == dbname.upw:
            return HttpResponse('登录成功')





def record(request):
    return render(request,'liuyan_01/record.html',{'b':'b'})

def record01(request):
    name = request.POST.get("name","")
    pw = request.POST.get("password","")

    db = models.use()
    db.uname = name
    db.upw = pw
    db.save()

    return redirect(reverse("liuyan_01:login"))

def edit(request):
    return render(request,'liuyan_01/edit.html',{'b':'b'})


def edit01(request):
    # uname = models.CharField(max_length=1000j
    # upw = models.CharField(max_length=1000)
    # uliuyan = models.TextField()


    # lname = models.CharField(max_length=1000)
    # lemil = models.CharField(max_length=1000)
    # laddrees = models.CharField(max_length=1000)
    # ltext = models.TextField()

    name = request.POST.get("name","")
    emil = request.POST.get("password","")
    addrees = request.POST.get("addrees","")
    text = request.POST.get("text","")


    db = models.liuyan()
    db.lname = name
    db.lemil = emil
    db.laddrees = addrees
    db.ltext = text
    db.save()

    return redirect(reverse("liuyan_01:index"))
