from django import forms

from users.models import Practicing

# class PracticingForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     address = forms.CharField(max_length=300)
#     phone_number = forms.CharField(max_length=20)
#     email = forms.EmailField()
    
class  PracticingForm(forms.ModelForm):
    
    class Meta:
        model = Practicing
        fields = ('__all__')
