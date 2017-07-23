from django.contrib import admin
from .models import Level
class LevelAdmin(admin.ModelAdmin):
	list_display = ('key_level','name')	
	prepopulated_fields = {'slug':('name',),}
admin.site.register(Level, LevelAdmin)

# Register your models here.
