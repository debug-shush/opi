from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    roll_no = models.CharField(max_length=20, default='0000')
    contact = models.CharField(max_length=20, default=False)

    def __str__(self):
        return self.username


class Technoplayer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    focus = models.IntegerField(blank=True, null=True)
    connection = models.IntegerField(blank=True, null=True)
    happiness = models.IntegerField(blank=True, null=True)
    loan = models.IntegerField(blank=True, null=True)
    # crossword = jsonfield.JSONField()
