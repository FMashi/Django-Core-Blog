from django.contrib import admin
from .models import Category,Comment,Post,Tag
from django.template.defaultfilters import slugify


def copy_posts(self, request, queryset):
    for post in queryset:
        # Create a new instance with a new primary key
        new_post = post
        new_post.pk = None
        new_post.id = None  # Set id to None to ensure a new record is created

        # Generate a unique title and slug for the new post
        original_title = new_post.title
        original_slug = new_post.slug
        new_title = f"{original_title} (Copy)"
        new_slug = slugify(original_slug)

        # Check if the new title or slug is not unique and append a counter
        counter = 1
        while Post.objects.filter(title=new_title).exists() or Post.objects.filter(slug=new_slug).exists():
            new_title = f"{original_title} (Copy {counter})"
            new_slug = f"{slugify(original_slug)}-{counter}"
            counter += 1

        new_post.title = new_title
        new_post.slug = new_slug
        new_post.save()


copy_posts.short_description = "Copy selected posts"  # Action description



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'active')
    list_filter = ('active', 'created', 'author', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    ordering = ('active', 'created')
    actions = [copy_posts]

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

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created', 'approved_comment')
    list_filter = ('approved_comment', 'created', 'author')
    search_fields = ('author', 'content')
    ordering = ('approved_comment', 'created')



