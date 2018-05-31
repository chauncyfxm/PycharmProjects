from django.db import models

# Create your models here.
class BookInfoisDeleteYes(models.Manager):
    def get_queryset(self):
        return super(BookInfoisDeleteYes,self).get_queryset().filter(isDelete = True)
class BookInfoisDeleteNot(models.Manager):
    def get_queryset(self):
        return super(BookInfoisDeleteNot,self).get_queryset().filter(isDelete = False)

class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset()
    def create(self,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.save()
    def isDelete(self, pk):
        b = self.get(pk)
        b.delete()
    def set(self, pk, btitle):
        b = self.get(pk = pk)
        b.btitle = btitle
        b.save()


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, db_column='mybtitle')
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    bookisDeleteYes = BookInfoisDeleteYes()
    bookisDeleteNot = BookInfoisDeleteNot()
    bookSelect = BookInfoManager()
    def __str__(self):
        return self.btitle
    class Meta():
        db_table = 'mybookInfo'
        ordering = ['-id']


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')
    def gender(self):
        if self.hgender:
            return'男'
        else:
            return '女'
    gender.short_description = "性别"
    def __str__(self):
        return self.hname
