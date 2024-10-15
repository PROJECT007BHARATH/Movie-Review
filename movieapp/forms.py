from django import forms
from .models import movie
from .models import Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = movie
        fields = ['category', 'Movie_Name', 'Release_date', 'Trailer', 'Description', 'Actors', 'Poster']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["author","stars","comment"]
