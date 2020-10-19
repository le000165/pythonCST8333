from django import forms
from .models import CovidCase
from django.conf import settings
# Create your views here.
# Author: The Dai Phong Le
# Date: 2020-09-25
# File name: CovidCase.py
# Assignment 1 Python


class CovidForm(forms.ModelForm):
    """
    Covid form will be the form for creating and updating
    inherits from the ModelForm
    """
    # date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        """
        Inner class for the CovidForm for the purpose of initializing
        """
        model = CovidCase
        fields = ('country_id', 'date', 'cases', 'deaths', 'name_fr', 'name_en')
        labels = {
            'country_id': 'Country Id',
            'date': 'Date',
            'cases': 'Cases',
            'deaths': 'Deaths',
            'name_fr': 'Name_fr',
            'name_en': 'Name_en'
        }

    def __init__(self, *args, **kwargs):
        super(CovidForm, self).__init__(*args, **kwargs)
        # self.fields['date'] = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        # print(settings.DATE_INPUT_FORMATS)
