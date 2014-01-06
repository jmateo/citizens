from django.db import models

# Create your models here.

class Community(models.Model):
    name =  models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Community'
        verbose_name_plural = 'Communities'


class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200) 
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    postalCode = models.CharField(max_length=100)
    email = models.EmailField()
    community = models.ManyToManyField(Community, verbose_name="list of communities")

class Concern(models.Model):
    name = models.CharField(max_length=200)
    positiveVotes = models.IntegerField(default=0)
    negativeVotes = models.IntegerField(default=0)
    created_by = models.ForeignKey(User) 
    
