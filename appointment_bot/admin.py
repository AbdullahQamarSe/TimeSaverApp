from django.contrib import admin
from .models import data_model



class OrderAdmin(admin.ModelAdmin):
    list_display = ("name","province","procedure","appointment")
    
admin.site.register(data_model,OrderAdmin)    