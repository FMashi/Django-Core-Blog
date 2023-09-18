import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from uuid import uuid4
from ckeditor.fields import RichTextField
from django.utils.deconstruct import deconstructible

@deconstructible
class PathRename(object):
    def __init__(self, sub_path):
        self.path = sub_path
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


ACTIVE = (
    (True, "Publish"),
    (False, "Draft"),
)
Grade = [
    ('excellent', 1),
    ('average', 0),
    ('bad', -1)
]

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Category Name')
    image = models.ImageField(null=True, blank=True, upload_to=PathRename('images/blog/Categories'),
                              verbose_name='Category Image')
    slug = models.SlugField(blank=True, allow_unicode=True, max_length=250, unique=True, null=True, verbose_name='Slug')
    active = models.BooleanField(default=False, choices=ACTIVE, verbose_name='Status')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/category/{}'.format(self.slug)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Tag Name')
    image = models.ImageField(null=True, blank=True, upload_to=PathRename('images/blog/Tags'),
                              verbose_name='Category Image')
    slug = models.SlugField(blank=True, allow_unicode=True, max_length=250, unique=True, null=True, verbose_name='Slug')
    active = models.BooleanField(default=False, choices=ACTIVE, verbose_name='Status')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/tag/{}'.format(self.slug)

class Post(models.Model):
    category = models.ManyToManyField(Category, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True, allow_unicode=True, max_length=250, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to=PathRename('images/blog/posts/'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')
    content = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=False, choices=ACTIVE, verbose_name='Status')
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    rating = models.CharField(choices=Grade, default='average', max_length=50)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-created']
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return '/post_detail/{}'.format(self.slug)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    rating = models.CharField(choices=Grade, default='average', max_length=50)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.post.pk})

    def __str__(self):
        return self.content[:20]


