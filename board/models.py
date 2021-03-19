from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    createDate = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modifiedDate = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    createDate = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modifyDate = models.DateTimeField(null=True, blank=True)
