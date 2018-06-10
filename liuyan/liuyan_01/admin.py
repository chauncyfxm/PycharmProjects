from django.contrib import admin

# Register your models here.
from .models import *

class useModelAdmin(admin.ModelAdmin):
    list_display = ['id','uname','upw','uliuyan']


admin.site.register(use,useModelAdmin)



