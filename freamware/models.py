from django.db import models
from django.contrib.auth.models import User
import tagging


default_length = 250

class Picture(models.Model):
	title         = models.CharField(max_length=default_length)
	description   = models.CharField(max_length=default_length)
	creation_time = models.DateTimeField(auto_now_add=True)
	user          = models.ForeignKey(User)
	url           = models.CharField(max_length=default_length)
	slug          = models.SlugField()

try:
	tagging.register(Picture)
except tagging.AlreadyRegistered:
	pass