from django.db import models
from django.contrib.auth.models import User

class project(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class user_project(models.Model):
    
    # This is the only required field
    #user = models.ForeignKey(User, unique=True)
    user = models.ForeignKey(User)

    # The rest is completely up to you
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title
    
