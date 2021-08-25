from django import forms
from django.forms import ModelForm
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'img_url']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
attrs={'class':'form-control', 'placeholder':'Selecta date',
'type':'date'}),
    }