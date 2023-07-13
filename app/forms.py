from typing import Any, Dict
from django import forms
from django.core import validators

def validate_for_a(svalue):
    if svalue[0] == 'a':
        raise forms.ValidationError('name is starting with a')

# def validate_for_len(name):
#     if len(name) <=5:
#         raise forms.ValidationError('len is less then 5')
    
# def validate_upper_letter(name):
#     if name [0].isupper():
#         raise forms.ValidationError('name not start with upper letter')

g = [('MALE','male'),('FEMALE','female'),('OTHERS','others')]
class StudentForms(forms.Form):
    sname = forms.CharField(max_length=100,validators=[validate_for_a,validators.MinLengthValidator(5)])
    sage = forms.IntegerField()
    gmail = forms.EmailField(validators=[validate_for_a])
    re_gmail =forms.EmailField()
    phone_no = forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    bot = forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    gender =forms.ChoiceField(choices=g,widget=forms.RadioSelect)

    def clean(self):
        e = self.cleaned_data['gmail']
        re = self.cleaned_data['re_gmail']
        if e != re :
            raise forms.ValidationError('gmails or not matched')
        

    def clean_bot(self):
        bote = self.cleaned_data['bot']
        if len(bote)>0:
            raise forms.ValidationError('not')