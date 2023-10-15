from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=50, null=True)
    email = models.EmailField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.fname