from django.contrib import admin
from .models import CustomUser, MyModel, AppleVariety

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(MyModel)
admin.site.register(AppleVariety)

