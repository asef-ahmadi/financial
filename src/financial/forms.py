from django import forms
from .models import Reciept
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class RecieptForm(forms.ModelForm):

    class Meta:
        model = Reciept
        fields = '__all__'
        localized_fields = '__all__'

        widgets = {
            'p': forms.NumberInput(attrs={'class': 'form-control font-vazir-fadigit'}),
            'amount': forms.NumberInput(attrs={'type': 'text', 'class': 'form-control font-vazir-fadigit', 'onkeyup': 'javascript:this.value=itpro(this.value);'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control font-vazir-fadigit'}),
        }
