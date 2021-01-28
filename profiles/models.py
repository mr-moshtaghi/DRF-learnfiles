from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)

    def __str__(self):
        return u'%s - %s' % (self.first_name, self.last_name)