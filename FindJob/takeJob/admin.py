from django.contrib import admin

# Register your models here.
from .models import ItJobs,UserBot

admin.site.register(ItJobs)
admin.site.register(UserBot)