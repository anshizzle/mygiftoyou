from django.db import models

# Create your models here.

class Gif(models.Model):
    gif_url = models.CharField(max_length=200)
    thread_url = models.CharField(max_length=200)
    upvotes = models.IntegerField
    downvotes = models.IntegerField
    subreddit = models.IntegerField
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

class Keyword(models.Model):
	gif = models.ForeignKey(Gif)
	keyword = models.CharField(max_length=100)
	score = models.IntegerField


class User(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class Vote(models.Model):
	user = models.ForeignKey(User)
	image = models.ForeignKey(Gif)
	liked = models.BooleanField