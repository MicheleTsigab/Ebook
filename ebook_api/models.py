from cgi import print_exception
from distutils.command.config import LANG_EXT
from turtle import title
from django.db import models
from django.contrib.auth.models import User
class customer(models.Model):
    customer=models.OneToOneField(User,on_delete=models.CASCADE)  
class author(models.Model):
    customer=models.OneToOneField(User,on_delete=models.CASCADE)
class ebook(models.Model):
    cover=models.ImageField()
    title=models.CharField(max_length=100)
    year=models.DateField(auto_now_add=True)
    price=models.FloatEbookApiConfigField() 
    path=models.FileField() 
    lang=models.CharField(max_length=30) 
    genre=models.ManyToManyField('genre',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class ebook_authored(models.Model):
    ebook=models.ForeignKey(ebook,on_delete=models.CASCADE)
    author=models.ForeignKey(author,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
class ebook_bought(models.Model):
    ebook=models.ForeignKey(ebook)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
class genre(models.Model):
    genre=models.CharField(max_length=50)
    sub_genre=models.CharField(max_length=50)
class reviews(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    ebook=models.ForeignKey(ebook,on_delete=models.CASCADE)
    rate=models.SmallIntegerField()
    date=models.DateField(auto_now_add=True)
    reviews=models.TextField()
class discounts(models.Model):
    discount=models.FloatField()

