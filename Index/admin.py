from django.contrib import admin

# Register your models here.
from .models import About
from .models import slider_display
from .models import client_detail

admin.site.register(About)
admin.site.register(slider_display)
admin.site.register(client_detail)

