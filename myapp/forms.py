from django import forms
from.models import User

class Students(forms.ModelForm):
    class Meta:
        model=User
        fields=['Name','Email','Password']
