from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.content

