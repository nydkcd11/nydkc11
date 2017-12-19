#admin registration page for Blog Application
from django.contrib import admin
from .models import Post, Video, Link, Image, Article
from embed_video.admin import AdminVideoMixin #module for Youtube Videos

#classes like these add customization to the admin's look and feel.
class ImageAdmin(admin.ModelAdmin):
	list_display = ('title','pub_date','show_home','post')#what displays on the table
	ordering = ('-post',)#default ordering for object listings
	filter_horizontal=('other_post',)#additional options to sort
	def pub_date(self, obj):
		return obj.post.pub_date_2
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','author','date')
class LinkAdmin(admin.ModelAdmin):
	list_display=('name','host','event_choices','show_screen')
	filter_horizontal=('other_link',)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','author','pub_date_2')
class VideoAdmin(AdminVideoMixin,admin.ModelAdmin):
	list_display = ('post_title', 'post_date')
	filter_horizontal=('post_related',)
	def post_title(self, obj):
		return obj.post.title
	def post_date(self, obj):
		return obj.post.pub_date_2

#models registered here. note that class AND model is registered
admin.site.register(Post, PostAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Article, ArticleAdmin)
# Register your models here.
