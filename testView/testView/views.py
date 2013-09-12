from django.http import HttpResponse, Http404
#from django.template import Template, Context
#from django.template.loader import get_template
import datetime
from django.shortcuts import render

def hello(request):
	return HttpResponse("Hello World")
	
	
#def current_datetime(request):
	#now = datetime.datetime.now()
	#html = "<html><body> It is now %s.</body></html>" % now
	#t = Template("<html><body> It is now {{ current_date }}. </body></html>")
	#t = get_template('current_datetime.html')
	#html = t.render(Context({'current_date': now}))
	#return HttpResponse(html)
	
	
def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'current_datetime.html', {'current_date': now})
	
	
#def hours_ahead(request, offset):
#	try:
#		Offset = int(offset)
#	except ValueError:
#		raise Http404()
		
#	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#	html = "<html><body> In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#	return HttpResponse(html)
	
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
		
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})