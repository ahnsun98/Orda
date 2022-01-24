from django.db import models
from django.db.models.fields import IntegerField, TextField, FloatField

class Mountain(models.Model):
    id = IntegerField(primary_key=True)
    name = TextField(null=True)
    loc = TextField(null=True)
    height = TextField(null=True)
    overview = TextField(null=True)
    routeimglink = TextField(null=True)
    detail = TextField(null=True)
    tourism = TextField(null=True)
    tourismimglink = TextField(null=True)
    lat = FloatField()
    lng = FloatField()
    
    class Meta:
        db_table = 'mountain'
        managed = False
        
    def __str__(self):
        return self.name
