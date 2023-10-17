from django.db import models
class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(unique=True)
    email = models.EmailField()
    address = models.TextField(max_length=300)
