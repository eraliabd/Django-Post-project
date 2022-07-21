from django import forms
from .models import Comment

class EmailPostForm(forms.Form):  # (models.Model - sql kodlarga o'tkazardi) bu esa forms.Form - bu html kodlarga o'tkazib qo'yadi.
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')