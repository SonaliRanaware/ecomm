from django.db import models
#create table stud(name varchar(20),email varchar(20),mobile int,msg varchar(20));----mysql
# Create your models here.
class stud(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    msg=models.CharField(max_length=500)
    
