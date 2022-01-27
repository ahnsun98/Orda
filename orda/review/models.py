from django.db import models
from django.db.models.fields import IntegerField, TextField, CharField


class Post(models.Model):
    id = IntegerField(primary_key=True)
    author = models.ForeignKey("account.BoardMember", on_delete=models.CASCADE,max_length=10, null=True, db_column="author")
    title = models.CharField(max_length=100, null=False, blank=False)
    m_name = TextField(null=True)
    m_loc = TextField(null=True)
    contents = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    file = models.ImageField(upload_to="",null=True)

