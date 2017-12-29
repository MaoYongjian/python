from django.db import models

# Create your models here.
class Message(models.Model):
	username = models.CharField(max_length=256)
	title = models.CharField(max_length=512)
	content = models.TextField()
	publish_date = models.DateTimeField()

	def __str__():
		return '{},{},{},{}'.format(self.username, self.title,self.content,self.publish_date)				