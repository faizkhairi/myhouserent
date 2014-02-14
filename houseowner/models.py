from django.db import models

# Create your models here.

class HouseOwner(models.Model):
    Full_Name = models.CharField(max_length=200)
    No_of_renters  = models.IntegerField(default=0)
    Houseownerjoinedthesite = models.DateTimeField('House owner join site')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.Full_Name