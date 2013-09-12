from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 255)
	slug = models.SlugField(unique = True, max_length = 255)
	description = models.CharField(max_length = 255)
	content = models.TextField()
	published = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		### how the model class should be ordered
		ordering = ['-created']
		
	def __unicode__(self):
	### used to display the objects to humans
		return u'%s' %self.title
			
	def get_absolute_url(self):
	### needed to link to a specific blog post
		return reverse('blog.views.post', args=[self.slug])

	
