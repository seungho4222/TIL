from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    genre = forms.ChoiceField(choices=[
        ('Comdey', 'Comedy'),
        ('Fantasy', 'Fantasy'),
        ('Romance', 'Romance'),
    ])

    score = forms.FloatField(
        required=False,
        min_value=0,
        max_value=5,
        widget=forms.NumberInput(
            attrs={'step': '0.5'}
        )
    )

    class Meta:
        model = Movie
        exclude = ('user',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)