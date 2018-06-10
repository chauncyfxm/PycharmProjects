from django.db import models

# Create your models here.


class use(models.Model):
    uname = models.CharField(max_length=1000)
    upw = models.CharField(max_length=1000)
    uliuyan = models.TextField()
    class Meta():
        db_table = 'use'



class liuyan(models.Model):
    lname = models.CharField(max_length=1000)
    lemil = models.CharField(max_length=1000)
    laddrees = models.CharField(max_length=1000)
    ltext = models.TextField()
    class Meta():
        db_table = 'liuyan'
