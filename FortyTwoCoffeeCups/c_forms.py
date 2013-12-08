from FortyTwoCoffeeCups.models import PersonBio
from django import forms
from django.forms import ModelForm


class PersonBioForm(ModelForm):

    class Meta:
        model = PersonBio
        fields = ['name',
                  'surname',
                  'date_of_birth',
                  'bio',
                  'email',
                  'photo',
                  'skype_id',
                  'jabber_id',
                  'other_contacts',
                  ]


class LoginForm(forms.Form):

    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
