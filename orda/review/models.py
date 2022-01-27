from django.db import models
from django.db.models.fields import IntegerField, TextField, CharField

<<<<<<< HEAD
=======
from account.models import BoardMember
>>>>>>> notsalhoon2

class Post(models.Model):
    id = IntegerField(primary_key=True)
    author = models.CharField(max_length=10, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    m_name = TextField(null=True)
    m_loc = TextField(null=True)
    contents = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
<<<<<<< HEAD
    file = models.FileField(null = True)
=======
    boardMember = models.ForeignKey(BoardMember, on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'post'
        app_label = 'review'
        managed = False
        
    def __str__(self):
        return self.id
>>>>>>> notsalhoon2

