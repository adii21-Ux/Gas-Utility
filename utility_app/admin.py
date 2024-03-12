from django.contrib import admin
from .models import CustomUser, ServiceRequest
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(ServiceRequest)