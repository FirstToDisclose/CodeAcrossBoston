from django.contrib.auth.models import User

from django.db import models

class Disclosure(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    body = models.TextField()

    owner = models.ForeignKey(User)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
