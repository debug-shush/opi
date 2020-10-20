from django.db import models
from django.contrib.auth.models import  User



# Create your models here.

# class User(models.Model):
# 	first_name = ..
# 	last_name = ..
# 	roll_no = 
#     passward =
     
class Thirdyear(models.Model):
	# user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	puzzle_score = models.CharField(max_length=10, blank=True, null=True)
	age_sum = models.BooleanField(max_length=10, blank=True)
	letter_sum = models.BooleanField(max_length=10, blank=True)
	# crossword = jsonfield.JSONField()

# class Firstyear(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
# 	puzzle_score = models.CharField(max_length=10, blank=True, null=True)
# 	age_sum = models.BooleanField(max_length=10, blank=True)
# 	letter_sum = models.BooleanField(max_length=10, blank=True)
