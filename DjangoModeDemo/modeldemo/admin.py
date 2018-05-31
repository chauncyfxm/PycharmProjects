from django.contrib import admin
from modeldemo.models import BookInfo,HeroInfo

class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    exta = 2
    # list_per_page = 3
    list_display = ['hname','hgender','hcontent']
    fields = [('hname','hgender'),'hcontent']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname','gender','hcontent']

class BookInAdmin(admin.ModelAdmin):
    list_display = ['btitle','pk','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    # fields = ['bpub_date','btitle']
    fieldsets = [('basic',{'fields':['btitle']}),('more',{'fields':['bpub_date']})]

    inlines = [HeroInfoInline]

admin.site.register(BookInfo,BookInAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
