from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
	user = models.OneToOneField(User)
	nickname = models.CharField(max_length = 16)
	permission = models.IntegerField()

	def __unicode__(self):
		return self.user.username

class Book(models.Model):
	name = models.CharField(max_length = 128)
	author = models.CharField(max_length = 128)
	typ = models.CharField(max_length = 128)
        link = models.TextField()
        code = models.TextField()


	class META:
		ordering = ['name']

	def __unicode__(self):
		return self.name
