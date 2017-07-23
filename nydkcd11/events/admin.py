from django.contrib import admin
from .models import DTC, List 
class ListAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',),}
admin.site.register(DTC)
admin.site.register(List, ListAdmin)
# Register your models here.
