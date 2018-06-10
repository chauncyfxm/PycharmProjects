from django.contrib import admin

# Register your models here.

# 幻灯片
from blogapp.models import Banner,Post,BlogCategory,Tags,Comment,FriendlyLink
admin.site.register(Banner)
admin.site.register(BlogCategory)
admin.site.register(Tags)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FriendlyLink)


