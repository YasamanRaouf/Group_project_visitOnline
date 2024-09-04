from django.db import models


class Comment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
