from django.db import models
import datetime

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    highest_education = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    major = models.CharField(max_length=20)
    university = models.CharField(max_length=100)
    experience_abroad = models.CharField(max_length=10)
    target_working_place = models.CharField(max_length=100)
    type_of_job = models.CharField(max_length=100)
    job_position_wanted = models.CharField(max_length=100)
    email = models.EmailField()
    time_of_graduation = models.DateField()
    birthdate = models.DateField()
    political_info = models.CharField(max_length=100)
    highest_title_achieved = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')



    def __str__(self):
        return self.name