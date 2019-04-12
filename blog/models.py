from django.db import models
import datetime


class Blog(models.Model):
    title = models.CharField(max_length=200, default='Title')
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    body = models.TextField(default="foobar")
    image = models.ImageField(upload_to='images/')