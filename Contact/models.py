from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, blank = False)
    email = models.CharField(max_length=100, blank = False)
    subject = models.CharField(max_length=500, blank=False)
    message = models.TextField(max_length=1000, blank = False)

    def __str__(self):
        return self.subject