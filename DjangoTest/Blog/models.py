from django.db import models

# Create your models here.

class Table(models.Model):
    title = models.TextField();
    content = models.TextField();
    SignTime = models.TimeField(auto_now=True);
