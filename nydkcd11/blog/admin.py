from django.contrib import admin
from .models import Post, Video, Link, Image, Article
class ImageAdmin(admin.ModelAdmin):
	list_display = ('title','pub_date','post')
	ordering = ('-post',)
	def pub_date(self, obj):
		return obj.post.pub_date
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','author','date')
class LinkAdmin(admin.ModelAdmin):
	list_display=('name','host','event_choices')
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','author','pub_date')
admin.site.register(Post, PostAdmin)
admin.site.register(Video)
admin.site.register(Link, LinkAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Article, ArticleAdmin)
# Register your models here.
