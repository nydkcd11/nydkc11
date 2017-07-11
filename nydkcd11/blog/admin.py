from django.contrib import admin
from .models import Post, Video, Link, Image, Article
from embed_video.admin import AdminVideoMixin
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
	list_display = ('title','author','pub_date_2')
class VideoAdmin(AdminVideoMixin,admin.ModelAdmin):
	list_display = ('post_title', 'post_date')
	def post_title(self, obj):
		return obj.post.title
	def post_date(self, obj):
		return obj.post.pub_date
admin.site.register(Post, PostAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Article, ArticleAdmin)
# Register your models here.
