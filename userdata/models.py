from django.db import models
from django.utils import timezone

class Subdomain(models.Model):
    subdomain = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    token = models.CharField(max_length=300)
    requester_id = models.TextField()
    descriptions = models.TextField()
    subjects = models.TextField()


    