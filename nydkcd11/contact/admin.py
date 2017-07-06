from django.contrib import admin
from .models import Contact, Email
class ContactAdmin(admin.ModelAdmin):
	list_display = ('title','name','email')
admin.site.register(Contact, ContactAdmin)
admin.site.register(Email)
# Register your models here.
