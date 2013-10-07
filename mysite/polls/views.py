# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse("Hello, world!!!! L33t")



def welcome(request):
	return HttpResponse('Hi there, you are in the page: ' + request.path + "\n Remote address: " + request.META['REMOTE_ADDR'])
	
	
	
def search_form(request):
	return render(request, 'search_form.html')
	
	
def search(request):
	print request.GET.items()
	
	if 'q' in request.GET:
		message = "You searched for : %r" %request.GET['q']
		
	else:
		message = "You submitted an empty form."
		
	
		
	return HttpResponse(message)