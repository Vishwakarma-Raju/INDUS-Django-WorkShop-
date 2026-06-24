from django.db import models

# Create your models here.

class student(models.Model):
    sname = models.CharField("Name", max_length=30)
    smobile = models.CharField( "Mobile", max_length=10)
    semail = models.EmailField("Email")
    saddress = models.CharField("Address")

def __str__(self):
    return self.sname

class Category(models.Model):
    title = models.CharField(max_length=100)

def __str__(self):
    return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    price = models.IntegerField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

def __str__(self):
    return self.title

