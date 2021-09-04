from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=90, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    image = models.ImageField(upload_to='about_Image/', blank=False)

    def __str__(self):
        return self.title

class slider_display(models.Model):
    title = models.CharField(max_length=90, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    image = models.ImageField(upload_to='slider_images/', blank=False)

    def __str__(self):
        return self.title


class client_detail(models.Model):
    name = models.CharField(max_length=40, blank=False)
    links = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='client_images/', blank=False)

    def __str__(self):
        return self.name

   

