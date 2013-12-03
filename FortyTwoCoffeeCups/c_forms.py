from FortyTwoCoffeeCups import models
from django import forms
from django.forms import ModelForm, widgets


class PersonBioForm(ModelForm):

    class Meta:
        model = models.PersonBio

    name = forms.CharField()
    surname = forms.CharField()
    date_of_birth = forms.DateField(input_formats=['%Y-%m-%d',])
    bio = forms.Textarea()
    email = forms.EmailField()
    skype_id = forms.CharField()
    jabber_id = forms.CharField()
    other_contacts = forms.Textarea()