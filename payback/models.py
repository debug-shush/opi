from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Technoplayer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    rollno = models.CharField(max_length=1, null=True)
    password = models.CharField(max_length=5,null=True)
    focus = models.IntegerField(blank=True, null=True)
    connection = models.IntegerField(blank=True, null=True)
    happiness = models.IntegerField(blank=True, null=True)
    loan = models.IntegerField(blank=True, null=True)
    # crossword = jsonfield.JSONField()
