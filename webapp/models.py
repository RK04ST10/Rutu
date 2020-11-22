from django.db import models

# Create your models here.


class BookTable(models.Model):
    Name = models.CharField(max_length=20)
    People = models.IntegerField()
    Task = models.CharField(max_length=20)


class Contact(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Msg = models.CharField(max_length=20)