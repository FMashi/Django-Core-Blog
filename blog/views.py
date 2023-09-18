
from django.core.paginator import Paginator
from .models import Post, Category, Comment, Tag
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.encoding import uri_to_iri
from django.template.response import TemplateResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
def search(request):
    query = request.GET.get('q')
    if query:
        post_results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct()
        category_results = Category.objects.filter(
            Q(name__icontains=query)
        ).distinct()
        tag_results = Tag.objects.filter(
            Q(name__icontains=query)
        ).distinct()

        context = {
            'query': query,
            'post_results': post_results,
            'category_results': category_results,
            'tag_results': tag_results,
            'nav_active': 'search',
        }
    else:
        context = {}

    template = 'blog/search.html'
    return render(request, template, context)

def blog(request,):
    posts = Post.objects.filter(active=True).order_by('-created')
    categories = Category.objects.filter(active=True).order_by('-created')
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Blog',
        'posts': posts,
        'categories': categories,
        'page_obj': page_obj,
        'nav_active': 'blog',
    }
    template = 'blog/index.html'
    return render(request, template, context)

@csrf_exempt
def blog_post(request, slug):
    post = get_object_or_404(Post, slug=uri_to_iri(slug), active=True)
    categories = Category.objects.filter(active=True).order_by('-created')
    comments = Comment.objects.filter(post=post, approved_comment=True)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

    else:
        comment_form = CommentForm()

    context = {
        'title': post.title,
        'post': post,
        'categories': categories,
        'comments':comments,
        'comment_form': comment_form,
    }
    template = 'blog/post.html'
    return TemplateResponse(request, template, context)



def post_by_category(request, category_slug):
    categories = Category.objects.filter(active=True).order_by('-created')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category, active=True)
    context = {
        'title': category.name,
        'posts': posts,
        'categories': categories,
        'category': category,
        'nav_active': 'category',
    }
    template = 'blog/category.html'
    return render(request, template, context)
