from django import forms

def validate_for_a(svalue):
    if svalue[0] == 'a':
        raise forms.ValidationError('name is starting with a')

def validate_for_len(name):
    if len(name) <=5:
        raise forms.ValidationError('len is less then 5')
    
def validate_upper_letter(name):
    if name [0].isupper():
        raise forms.ValidationError('name not start with upper letter')

g = [('MALE','male'),('FEMALE','female'),('OTHERS','others')]
class StudentForms(forms.Form):
    sname = forms.CharField(max_length=100,validators=[validate_for_a,validate_for_len])
    sage = forms.IntegerField()
    gmail = forms.EmailField(validators=[validate_for_a,validate_upper_letter])
    gender =forms.ChoiceField(choices=g,widget=forms.RadioSelect)
