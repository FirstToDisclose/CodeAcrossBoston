from django.contrib.auth.models import User

from django.db import models

class Disclosure(models.Model):
    title = models.CharField(max_length=255)
    
    abstract = models.TextField(null=True)
    abstract_file = models.FileField(null=True)
    
    body = models.TextField(null=True)
    body_file = models.FileField(null=True)
    
    #to-do
    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
