from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

    def __init__(self, *args, **kwargs):
        self.doctor = kwargs.pop('doctor', None)
        self.visit = kwargs.pop('visit', None)
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        if self.doctor:
            comment.doctor = self.doctor
        if self.visit:
            comment.visit = self.visit
        comment.user = self.user
        if commit:
            comment.save()
        return comment
