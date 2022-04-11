from django.contrib import admin

# Register your models here.
from .models import contact

class main(admin.ModelAdmin):
    listd = ("your_name","your_email","your_sub","your_mess")

admin.site.register(contact,main)

class new(admin.ModelAdmin):
    list = ('full_name','message','email')