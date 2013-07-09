from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget

from django.contrib.auth.models import User
GENDER_CHOICES = (('female', 'Female'),('male', 'Male'))


class Registration_Form(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    gender = forms.MultipleChoiceField(required=True,widget=CheckboxSelectMultiple, choices=GENDER_CHOICES)

    def clean_username(self):
        newusername = self.cleaned_data['username']
        all_username = [] 
        all_user = User.objects.all()
        for u in all_user:
            all_username.append(u.username)

        if newusername in all_username:
            raise forms.ValidationError('This username is already used. Please select another username')
        
        return newusername
    
    def clean(self):
        cleaned_data = super(Registration_Form, self).clean()
        try:
            pwd1 = self.cleaned_data['password1']
            pwd2 = self.cleaned_data['password2']
            if pwd1 != pwd2:
                msg = "password not the same"
                self._errors["password1"] = self.error_class([msg])
                self._errors["password2"] = self.error_class([msg])
        except:
            pass
        return cleaned_data



