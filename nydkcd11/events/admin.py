from django.contrib import admin
from .models import DTC, List, Part, Convention
class ListAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',),}
admin.site.register(DTC)
admin.site.register(List, ListAdmin)
admin.site.register(Part)
admin.site.register(Convention)
# Register your models here.
