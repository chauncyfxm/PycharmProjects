from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.core.urlresolvers import reverse
from django.http import JsonResponse
# Create your views here.

# index
def index(request):
    list = models.Blog.objects.all()
    return render(request,"myBlog/index.html",{"list":list})

# editpage
def editpage(request):
    ses = request.session.get('uname')
    if ses:
        return render(request,"myBlog/editpage.html")
    else:
        return HttpResponse('请先登录')


# datail
def datail(request, id):
    object = models.Blog.objects.get(pk = id)
    return render(request, "myBlog/datail.html", {'object':object})

# editpagehandle
def editpagehandle(request):
    ses = request.session.get('uname')

    if ses:
        dbname = models.use.objects.get(uname=ses)
        title = request.POST.get("title","")
        content = request.POST.get("content","")

        db = models.Blog()
        db.btitle = title
        db.bcontent = content
        db.bpid = dbname
        db.save()

        return redirect(reverse('blog:index'))
    else:
        return HttpResponse('请先登录')

# login
def login(request):
    return render(request, 'myBlog/login.html')

# login_handle
def login_handle(request):


    name = request.POST.get("name","")
    pw = request.POST.get("pw","")

    try:
        dbname = models.use.objects.get(uname=name,upw=pw)
    except:
        return HttpResponse('账号或密码错误')
    else:
        if name == dbname.uname and pw == dbname.upw:
            request.session['uname'] = name
            return redirect(reverse('blog:index'))
        else:
            return HttpResponse('账号或密码错误')



# logout
def logout(request):
    # request.session['uname'] = None
    # del request.session['uname']
    # request.session.clear()
    request.session.flush()
    return redirect(reverse('blog:index'))


# record_handle
def record_handle(request):
    # uname = models.CharField(max_length=1000)
    # upw = models.CharField(max_length=1000)
    # uliuyan = models.TextField()

    name = request.POST.get('name','')
    pw = request.POST.get('pw','')
    print(pw)
    text = request.POST.get('text','')

    db = models.use()
    db.uname =  name
    db.upw = pw
    db.uliuyan = text
    db.save()

    return redirect(reverse('blog:login'))
# record
def record(request):
    return render(request,'myBlog/record.html')


# ajax
def ajax(request):
    name = request.session.get('uname')
    return JsonResponse({'v3':name})

# 自己的博客
def myblog(request):
    name = request.session.get('uname')

    if name:
        list = []
        db = models.Blog.objects.filter(bpid__uname=name)
        print(db)
        for i in db:
            # list.append([{'id':i.id},{'btitle':i.btitle}])
            list.append([i.id,i.btitle])


        list.append([0,'结尾'])
        return JsonResponse({'v3':list})
    return JsonResponse({'v3':''})
