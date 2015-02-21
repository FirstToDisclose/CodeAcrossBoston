from django.db import models

class Disclosure(models.Model):
    disclosure_text = models.CharField(max_length=200)
