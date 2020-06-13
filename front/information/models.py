from django.db import models

# Create your models here.

class information(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'information_db'