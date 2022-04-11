from django.db import models

# Create your models here.
class contact(models.Model):
    your_name = models.CharField(max_length=200)
    your_email= models.CharField(max_length=200)
    your_sub = models.CharField(max_length=150)
    your_mess = models.CharField(max_length=105)

class userform (models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    message=models.TextField()