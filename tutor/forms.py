from django import forms
from .models import Profile, Subject
from django.contrib.auth.forms import UserChangeForm

class List(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "email_addr", "phone_number", "subjects_can_help"]       

class EditProfile(UserChangeForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "email_addr", "phone_number", "subjects_can_help"]
   