from __future__ import unicode_literals

from django.db import models

# Create your models here.

#class Comments(models.Model):
#	userComent = models.TextField()

#	def __unicode__(self):
#		return self.userComent


class Post(models.Model):
	title = models.CharField(max_length=120)
	content=models.TextField()
	#content = models.ManyToManyField(Comments,null=True,blank=True)
	
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)


	def __unicode__(self):
		return self.title	













