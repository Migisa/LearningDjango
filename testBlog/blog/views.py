### Create your views here.
### create templates for each of the views

from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.http import HttpResponse


def index(request):
	### get the blog posts that are published
	posts = Post.objects.filter(published=True)
	
	### return the rendered template
	return render(request, 'blog/index.html', {'posts':posts})
	
	
def post(request, slug):
	### get the Post object
	post = get_object_or_404(Post, slug = slug)
	
	### now return the rendered template
	return render(request, 'blog/post.html', {'post': post})


def search_form(request):
	post = ""
	if 'q' in request.GET:
		if request.GET['q']:
			message = 'You searched for: %r' %request.GET['q']	
			q = request.GET['q']
			print q
			#post = Post.objects.filter(title__icontains = q)
			post = get_object_or_404(Post,slug = q)
			print post
		else:
			message = 'You submitted an empty form.'	
	else:
		message = ''
	print post
	return render(request, 'blog/search.html', {'message': message, 'post': post})
    
    
    
    