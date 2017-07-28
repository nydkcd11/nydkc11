from embed_video.admin import AdminVideoMixin
from django.contrib import admin
from .models import DTC, List, Part, Convention
class ListAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',),}
class ConventionAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass
class PartAdmin(admin.ModelAdmin):
	list_display = ('header', 'convention')	
admin.site.register(DTC)
admin.site.register(List, ListAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Convention, ConventionAdmin)
# Register your models here.
