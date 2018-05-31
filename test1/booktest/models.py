from django.db import models

# Create your models here.
class Bookinfo(models.Model):
    btitle = models.CharField(max_length = 200)
    bpub_date = models.DateTimeField()


    def __str__(self):
        return '%d' % self.pk


class HeroInfo(models.Model):
    hname = models.CharField(max_length = 200)
    hgender = models.BooleanField()
    hconter = models.CharField(max_length=200)
    hbook = models.ForeignKey('Bookinfo')

    def __str__(self):
        return "%d" % self.pk
