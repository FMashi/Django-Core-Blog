from django.contrib import admin
from .models import Category,Comment,Post,Tag
from django.template.defaultfilters import slugify
from django.utils.html import format_html

def make_draft(modeladmin, request, queryset):
    queryset.update(active=False)

make_draft.short_description = "Mark selected drafts"

def publish_posts(modeladmin, request, queryset):
    queryset.update(active=True)

publish_posts.short_description = "Publish selected"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('display_image','title', 'author', 'created', 'active')
    list_filter = ('active', 'created', 'author', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    ordering = ('active', 'created')
    actions = [make_draft, publish_posts]
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', obj.image.url)
        else:
            return 'No Image'
    display_image.short_description = 'Image'


    @admin.action(description='Mark selected posts as published')
    def make_published(self, request, queryset):
        queryset.update(active=True)

    @admin.action(description='Mark selected posts as draft')
    def make_draft(self, request, queryset):
        queryset.update(active=False)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    actions = [make_draft, publish_posts]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    actions = [make_draft, publish_posts]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created', 'approved_comment')
    list_filter = ('approved_comment', 'created', 'author')
    search_fields = ('author', 'content')
    ordering = ('approved_comment', 'created')
    actions = [make_draft, publish_posts]



