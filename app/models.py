from django.db import models

# Create your models here.
class school(models.Model):
    sclname = models.CharField(max_length=100,primary_key=True)
    pname=models.CharField(max_length=100)
    fee=models.IntegerField()

class student(models.Model):
    sclname=models.ForeignKey(school,on_delete=models.CASCADE)
    sno=models.IntegerField()
    saddress=models.CharField(max_length=50)
    sname=models.CharField(max_length=100)
