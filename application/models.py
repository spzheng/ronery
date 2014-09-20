from django.db import models

# Create your models here.
class Person(models.Model):
	phone = models.CharField(unique = true, primary_key = true) 
	active = models.BooleanField()
	gender = models.CharField(max_length = 1)
	age = models.IntegerField()
	interests = models.TextField()
	rating = models.IntegerField()
	safe_mode = models.BooleanField()
	def __unicode__(self):
		return self.title

class Conversation (models.Model):
	person1 = models.ForeignKey(Person, primary_key = true)
	person2 = models.ForeignKey(Person)
	def __unicode__(self):
		return self.post_text