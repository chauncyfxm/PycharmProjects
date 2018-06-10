from django.shortcuts import render
from . import models
from django.views.generic.base import View
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.


# 首页
def index(request):
    # 轮播图
    banner_list = models.Banner.objects.all()

    # 推荐博客
    recommend_list = models.Post.objects.filter(recommend = 1)

    # 最新发布
    post_list = models.Post.objects.order_by('-pub_date').all()[:10]

    # 博客分类
    blogcategory_list = models.BlogCategory.objects.all()

    # 最新评论博客列表
    comment_list = models.Comment.objects.order_by('-pub_date')
    new_comment_list = []
    for test in comment_list:
        if test.post not in new_comment_list:
            print(test.post)
            new_comment_list.append(test.post)


    # 友情链接
    friendlylink_list = models.FriendlyLink.objects.all()


    #--------------------------------------------------
    ctx = {
        'banner_list': banner_list,
        'recommend_list': recommend_list,
        'post_list': post_list,
        'blogcategory_list': blogcategory_list,
        'new_comment_list': new_comment_list,
        'friendlylink_list': friendlylink_list
    }
    return render(request, 'index.html', ctx)




# 搜索
class SearchView(View):
    # def get(self, request):
    #     pass
    def post(self, request):
        kw = request.POST.get('keyword')
        post_list = models.Post.objects.filter(Q(title__icontains=kw)|Q(content__icontains=kw))

        ctx = {
            'post_list': post_list
        }
        return render(request, 'list.html', ctx)


# 列表功能
class TagMessage(object):
    def __init__(self, tid, name, count):
        self.tid = tid
        self.name = name
        self.count = count

def blog_list(request,cid = -1):

    # 博客分类
    blogcategory_list = models.BlogCategory.objects.all()


    if cid != -1:
        blogCategory = models.BlogCategory.objects.all(id = cid)
        post_list = blogCategory.post_set.all()
    else:
        post_list = models.Post.objects.all()


    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(post_list, per_page=1, request=request)

    post_list = p.page(page)

    tags = models.Tags.objects.all()
    tag_message_list = []
    for t in tags:
        count = len(t.post_set.all())
        tm = TagMessage(t.id, t.name, count)
        tag_message_list.append(tm)

    ctx = {
        'post_list': post_list,
        'tags': tag_message_list,
        'blogcategory_list':blogcategory_list,

    }
    return render(request, 'list.html', ctx)


# 详情页
def blog_detail(request, bid):
    post = models.Post.objects.get(id=bid)
    print(post)
    post.views = post.views + 1
    post.save()

    # 评论
    # if request.POST.get('comment-textarea'):
    #     comment = models.Comment()
    #     comment.content = request.POST.get('comment-textarea')
    #     comment.user_id = 1
    #     comment.post_id = post.id
    #     comment.pub_date = datetime.now()
    #     comment.save()


    comment_list = post.comment_set.all()
    # 评论结束


    # 博客标签
    post_list = []
    tag_list = post.tags.all()
    for tag in tag_list:
        for i in tag.post_set.order_by('-pub_date').all()[:5]:
            post_list.append(i)

    ctx = {
        'post': post,
        'post_list':post_list,
        'comment_list':comment_list,
    }
    return render(request, 'show.html', ctx)
# 详情页结束

class CommentView(View):
    def get(self, request):
        pass
    def post(self, request, bid):

        comment = models.Comment()
        comment.user = request.user
        comment.post = models.Post.objects.get(id=bid)
        comment.content = request.POST.get('comment-textarea')
        comment.pub_date = datetime.now()
        comment.save()
        # Ajax
        return HttpResponseRedirect(reverse("blog:blog_detail", kwargs={"bid":bid}))





