from django.db import models

# Create your models here.

class student(models.Model):
    sname = models.CharField("Name", max_length=30)
    smobile = models.CharField( "Mobile", max_length=10)
    semail = models.EmailField("Email")
    saddress = models.CharField("Address")

def __str__(self):
        return self.sname