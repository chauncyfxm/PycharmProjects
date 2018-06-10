from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader
from .models import *
from django.utils import timezone
from datetime import *
# Create your views here.


def home(request):
    booklist = BookInfo.objects.all()
    template = loader.get_template('modeldemo/index.html')
    context = RequestContext(request,{'booklist':booklist})
    return HttpResponse(template.render(context))


def index(Request):
    # booklist = models.BookInfo.objects.all()
    # template = loader.get_template("modeldemo/a_01.html")
    # context = RequestContext(Request,{"booklist":booklist})
    # return HttpResponse(template.render(context))

    # models.BookInfo.bookSelect.set(id,"射雕英雄转")
    # booklist = models.BookInfo.bookisDeleteNot.all()[3:5]
    # models.BookInfo.bookSelect.create('啦啦啦啦啦',datetime(9013,11,23,12,12,12))
    # booklist = models.BookInfo.bookisDeleteNot.exists()
    # 比较运算符
    # booklist = models.BookInfo.bookisDeleteNot.filter(HeroInfo__hname__contains = '虚竹')
    # booklist = BookInfo.bookSelect.filter(heroinfo__hname = '虚竹')
    booklist = models.BookInfo.bookisDeleteNot.all().
    return render(Request,"modeldemo/a_48.html",{'booklist':booklist})

def datail(Request,id):
    book = BookInfo.bookisDeleteNot.get(pk=id)
    template = loader.get_template("modeldemo/a_02.html")
    context = RequestContext(Request,{'book':book})
    return HttpResponse(template.render(context))

