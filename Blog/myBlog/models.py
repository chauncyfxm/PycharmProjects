from django.db import models

# Create your models here.
class Blog(models.Model):
    btitle = models.CharField(max_length = 200)
    bcontent = models.TextField()
    bpid = models.ForeignKey('use')
    class Meta():
        db_table = "Blog"
    def __str__(self):
        return self.btitle
# use
class use(models.Model):
    uname = models.CharField(max_length=1000)
    upw = models.CharField(max_length=1000)
    uliuyan = models.TextField()
    class Meta():
        db_table = 'use'
    # def __str__(self):
    #     return self.id

