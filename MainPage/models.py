from django.db import models

# Create your models here.

class Rooms(models.Model):
    Roomno = models.IntegerField(primary_key=True)
    TYPES = [('S', 'Single'),('D','Double')]
    RoomType = models.CharField(choices=TYPES,max_length=10)
    STYPES = [('C','CLEANED'),('N','NOTCLEANED'),('O','OCCUPIED')]
    Status = models.CharField(default='C',choices=STYPES,max_length=10)
    Checkin = models.DateTimeField(null=True)
    Reserved = models.BooleanField(default=False)


