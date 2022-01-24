from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
class Mountain(models.Model):
    mountain_id = IntegerField()
    name = TextField()
    loc = TextField()
    height = TextField()
    overview = TextField()
    routeimglink = TextField()
    detail = TextField()
    tourism = TextField()
    tourismimglink = TextField()

    class Meta:
        db_table = 'info_mountain'
        managed = False
