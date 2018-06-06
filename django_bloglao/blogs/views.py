from django.shortcuts import render
from .models import Banner, Post, BlogCategory, Comment, FriendlyLink


# Create your views here.
def index(request):
    banner_list = Banner.objects.all()
    # 去数据库里面取出所有　推荐的文章
    recomment_list = Post.objects.filter(is_recomment=True)
    for recoment in recomment_list:
        recoment.content = recoment.content[:100] + '......'

    # 取出所有文章　按照时间倒序
    post_list = Post.objects.order_by('-pub_date')
    for post in post_list:
        post.content = post.content[:160] + '......'

    # 博客分类
    blogcategory_list = BlogCategory.objects.all()

    # 最新评论博客列表
    comment_list = Comment.objects.order_by('-pub_date')
    new_comment_list = []
    for test in comment_list:
        if test.post not in new_comment_list:
            new_comment_list.append(test.post)
    # # 空的博客列表
    # new_comment_list = []
    # # 临时的id列表
    # test_id_list = []
    # for test in comment_list:
    #     if test.post.id not in test_id_list:
    #         test_id_list.append(test.post.id)
    #         new_comment_list.append(test.post)
    # 友情链接
    friendlylink_list = FriendlyLink.objects.all()
    ctx = {
        'banner_list': banner_list,
        'recomment_list': recomment_list,
        'post_list': post_list,
        'blogcategory_list': blogcategory_list,
        'new_comment_list': new_comment_list,
        'friendlylink_list': friendlylink_list

    }
    return render(request, 'index.html', ctx)
