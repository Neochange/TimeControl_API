from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeBlock(models.Model):
    ssid = models.CharField(max_length=100)
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING)
    
    class Meta:
        # managed = False
        db_table = 'timeblock'
        
        
class Interval(models.Model):

    init_date = models.DateTimeField()
    fin_date = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)    

    class Meta:
        # managed = False
        db_table = 'interval'             