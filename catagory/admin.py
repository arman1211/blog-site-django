from django.contrib import admin
from catagory.models import Catagory

# Register your models here.
# admin.site.register(Catagory)

class CatagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name','slug']

admin.site.register(Catagory,CatagoryAdmin)