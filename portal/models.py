from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

################
# Patient Read Article
################
class article(models.Model):
    title = models.CharField(max_length = 200)
    authors = models.CharField(max_length = 200)
    text = models.TextField(max_length = 400)
    def __unicode__(self):
        return self.title


################
# Extra feild for user
################
class user_extra_field(models.Model):  
    user = models.OneToOneField(User)  
    #other fields here
    gender = models.CharField(max_length=100)

    def __str__(self):  
        return "%s's profile" % self.user  
