from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Comment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.CASCADE)
    visit = models.ForeignKey('doctor.Visit', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # Rating between 1 and 5
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'doctor', 'visit'], name='unique_user_doctor_visit')
        ]
        ordering = ['-created_at']
    
    def __str__(self):
        return 'Comment "{}" by {}'.format(self.text, self.user)
