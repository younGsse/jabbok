from django.db import models

# Create your models here.

class Novel(models.Model):
    # author, title, subtitle, creation time,
    author = models.CharField(max_length=50)
    title = models.TextField(max_length=100)
    subtitle = models.TextField(max_length=100)
    content = models.TextField(max_length=2000)
    createDate = models.DateTimeField()
    # need to depart title, subtitle, for manage
    # title ForeignKey, subtitle, content
