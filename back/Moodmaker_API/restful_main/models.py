from django.db import models

# Create your models here.

class information_board(models.Model):
    objects = models.Manager()
    no = models.AutoField(db_column='No', primary_key=True)
    title = models.CharField(db_column='TITLE', max_length=200)
    content = models.CharField(db_column='CONTENT', max_length=1000)