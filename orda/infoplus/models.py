from django.db import models

# Create your models here.
class Mountain(models.Model):
    name=models.CharField(max_length=20)
    loc = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    overview = models.CharField(max_length=20)
    routeimglink = models.CharField(max_length=20)
    detail =models.CharField(max_length=20)
    tourism = models.CharField(max_length=20)
    tourismimglink = models.CharField(max_length=20)
    lat=models.DecimalField(decimal_places=15,max_digits=30)
    lng=models.DecimalField(decimal_places=15,max_digits=30)
    class Meta:
        db_table='mountain'
        managed = False
    def __str__(self):
        return self.name
