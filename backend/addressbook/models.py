from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='images/', null=True)