from django.contrib import admin
from .models import Post, Comment # , CustomTaggedPost

# Register your models here.
# admin.site.register(Post) # inital/default way of registering Models

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'body', 'status']
    list_filter = ['status', 'created', 'author', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug' : ('title', )}
    raw_id_fields = ['author', ]
    date_hierarchy = 'publish' 
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
    
# @admin.register(CustomTaggedPost)
# class CustomTaggedPostAdmin(admin.ModelAdmin):
#     list_display = ('tag', 'content_object', 'object_id')
#     search_fields = ('tag__name', 'content_object__title')