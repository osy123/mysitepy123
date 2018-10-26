import MySQLdb
from django.db import models

# Create your models here.
from mysitepy.settings import DATABASES

class Board(models.Model):

    group_no = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now=True)
    title = models.CharField(max_length=5)
    content = models.TextField(max_length=200)
    hit = models.IntegerField(null=True)
    depth = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        #return self.title
        return 'Board(%d,%d,%s,%s,%s,%d,%s,%s)' %(self.group_no,self.order_no,self.reg_date,self.title,self.content,self.hit,self.depth,self.name)
