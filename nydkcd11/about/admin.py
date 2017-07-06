from django.contrib import admin
from .models import Division, School, FAQ
class DivisionAdmin(admin.ModelAdmin):
	list_display = ('name','position','school','email')
class SchoolAdmin(admin.ModelAdmin):
	list_display = ('school','pres','vicepres','secretary','treasurer','webmaster','editor')
admin.site.register(Division, DivisionAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(FAQ)
# Register your models here.
