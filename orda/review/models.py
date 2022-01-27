from django.db import models
from django.db.models.fields import IntegerField, TextField, CharField


class Post(models.Model):
    id = IntegerField(primary_key=True)
    author = models.CharField(max_length=10, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    m_name = TextField(null=True)
    m_loc = TextField(null=True)
    contents = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    file = models.FileField(null = True)

