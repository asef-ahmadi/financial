from django import forms
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            # 'p': forms.NumberInput(attrs={'class': 'form-control font-vazir-fadigit'}),
        }
