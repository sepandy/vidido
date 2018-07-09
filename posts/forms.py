from django import forms
from accounts.models import Profile
from .models import Post


class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text']
        exclude = ['shareDate', 'author']

        widgets = {
            'text':forms.Textarea(attrs={
                'placeholder': "what's in your mind...",
                'id': '#post-input-text',
                'class': 'post-input-textarea form-control center-content mb-2'
            })
        }