from django.contrib import admin
from .models import *
# Register your models here.


class Bloga(admin.ModelAdmin):
    list_display = ['btitle','id','bcontent','bpid']

class usea(admin.ModelAdmin):
    list_display = ['uname','id','upw','uliuyan']

admin.site.register(Blog,Bloga)
admin.site.register(use,usea)
