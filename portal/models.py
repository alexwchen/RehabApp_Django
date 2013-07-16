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


################
# User uploaded autdio file
################

def upload_to(instance, filename):
    return 'documents/%s/%s' % (instance.user.username, filename)

class user_audio(models.Model):
    user = models.ForeignKey(User)

    #other fields here
    docfile = models.FileField(upload_to=upload_to)
    #docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):  
        return 'documents/'+str(self.user)+'/%Y/%m/%d'


