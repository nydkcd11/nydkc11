#Admin Registration Page for the About section of the website
#This section envelops essentially the "About subsection" on the website.
from django.contrib import admin
from .models import Division, School, FAQ #note Models from models.py must be imported

#Additional Details are made via Admin classes, and are registered in addition to the model.
class DivisionAdmin(admin.ModelAdmin):
	list_display = ('name','position','school','email')
class SchoolAdmin(admin.ModelAdmin):
	list_display = ('school','pres','vicepres','secretary','treasurer','webmaster','editor')

#classes are registered here
admin.site.register(Division, DivisionAdmin) #note that the admin class was registered with the model
admin.site.register(School, SchoolAdmin)
admin.site.register(FAQ)
# Register your models here.
