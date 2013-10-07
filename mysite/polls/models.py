from django.db import models

# Create your models here.
### creates two models: Poll and Choice


class Poll(models.Model):
	#question = models.CharField(max_length = 200)
	#pub_data = models.DateTimeField("date published")
	
	#def __unicode__(self):
	#	return self.question
	print("These are your classes as you start building real apps")
	
	
class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	
	def __unicode__(self):
		return self.choice_text
		
		
class randomObj(models.Model):
	name = models.CharField(max_length = 20)
	surname = models.CharField(max_length = 30)
	
	
	def __unicode__(self):
		return (self.name, self.surname)
