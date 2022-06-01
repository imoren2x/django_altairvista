from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Facility)
admin.site.register(models.AltairProfile)
admin.site.register(models.Manufacturer)
admin.site.register(models.Television)
admin.site.register(models.Monitor)
admin.site.register(models.Product)
