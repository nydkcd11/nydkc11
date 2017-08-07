from embed_video.admin import AdminVideoMixin
from django.contrib import admin
from .models import List, Part, Convention, Service
class ListAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',),}
class ConventionAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass
class PartAdmin(admin.ModelAdmin):
	list_display = ('header', 'convention')	
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('title','school','location','start_time','end_time','all_day')
admin.site.register(List, ListAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Convention, ConventionAdmin)
admin.site.register(Service,ServiceAdmin)
# Register your models here.
