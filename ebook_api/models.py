
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
class customer(models.Model):
    customer=models.OneToOneField(User,on_delete=models.CASCADE) 
    bought_ebooks=models.ManyToManyField('ebook',through='bought_ebook') 
    def __str__(self):
        return self.customer.username
    
class author(models.Model):
    author=models.OneToOneField(User,on_delete=models.CASCADE)
    authored_ebooks=models.ManyToManyField('ebook',through='authored_ebook')
    def __str__(self):
        return self.author.username
class ebook(models.Model):
    cover=models.ImageField(blank=True,null=True)
    title=models.CharField(max_length=100)
    year=models.DateField(auto_now_add=True)
    price=models.FloatField() 
    path=models.FileField() 
    lang=models.CharField(max_length=30) 
    genre=models.ManyToManyField('genre')
    def __str__(self):
        return self.title
class authored_ebook(models.Model):
    ebook=models.ForeignKey(ebook,on_delete=models.CASCADE)
    author=models.ForeignKey(author,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.ebook.title + " by " + self.author.author.username
class bought_ebook(models.Model):
    ebook=models.ForeignKey(ebook,on_delete=models.CASCADE)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.ebook.title
class genre(models.Model):
    genre=models.CharField(max_length=50)
    sub_genre=models.CharField(max_length=50)
    def __str__(self):
        return self.genre
class review(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    ebook=models.ForeignKey(ebook,on_delete=models.CASCADE)
    rate=models.SmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    date=models.DateField(auto_now_add=True)
    review=models.TextField()
    def __str__(self):
        return self.review
class discount(models.Model):
    discount=models.FloatField()
    def __str__(self):
        return str(self.discount)+"%"

