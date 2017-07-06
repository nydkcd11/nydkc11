from django.contrib import admin
from .models import Post, Video, Link, Image, Article
class ImageAdmin(admin.ModelAdmin):
	list_display = ('title','pub_date','post')
	ordering = ('-post',)
	def pub_date(self, obj):
		return obj.post.pub_date
admin.site.register(Post)
admin.site.register(Video)
admin.site.register(Link)
admin.site.register(Image, ImageAdmin)
admin.site.register(Article)
# Register your models here.
