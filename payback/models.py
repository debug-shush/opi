from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    roll_no = models.CharField(max_length=20, default='0000')
    contact = models.CharField(max_length=20, default=False)

    def __str__(self):
        return self.username


class Technoplayer1(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    focus1 = models.IntegerField(blank=True, null=True)
    connection1 = models.IntegerField(blank=True, null=True)
    happiness1 = models.IntegerField(blank=True, null=True)
    loan1 = models.IntegerField(blank=True, null=True)
    # crossword = jsonfield.JSONField()

class Technoplayer2(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    focus2 = models.IntegerField(blank=True, null=True)
    connection2 = models.IntegerField(blank=True, null=True)
    happiness2 = models.IntegerField(blank=True, null=True)
    loan2 = models.IntegerField(blank=True, null=True)
    # crossword = jsonfield.JSONField()

class Technoplayer3(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    focus3 = models.IntegerField(blank=True, null=True)
    connection3 = models.IntegerField(blank=True, null=True)
    happiness3 = models.IntegerField(blank=True, null=True)
    loan3 = models.IntegerField(blank=True, null=True)
    # crossword = jsonfield.JSONField()

class Technoplayer4(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    focus4 = models.IntegerField(blank=True, null=True)
    connection4 = models.IntegerField(blank=True, null=True)
    happiness4 = models.IntegerField(blank=True, null=True)
    loan4 = models.IntegerField(blank=True, null=True)
    # crossword = jsonfield.JSONField()






