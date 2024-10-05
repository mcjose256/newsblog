from django.shortcuts import render, get_object_or_404
from .models import post  # Make sure to use the correct model name

def post_list(request):
    posts = post.published.all()  # Retrieve all published posts
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, slug):  # Changed parameter name to 'slug'
    # Ensure the slug is used correctly
    post_instance = get_object_or_404(post,  # Use the 'post' model
        slug=slug,  # Match the slug parameter from the URL
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(request, 'blog/post/detail.html', {'post': post_instance})  # Render with post_instance
