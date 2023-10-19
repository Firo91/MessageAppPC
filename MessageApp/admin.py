from django.contrib import admin
from .models import MyMessage, CustomUser

admin.site.register(MyMessage)
admin.site.register(CustomUser)
