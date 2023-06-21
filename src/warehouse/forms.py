from django import forms
from .models import ClothRoll
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class ClothRollForm(forms.ModelForm):

    class Meta:
        model = ClothRoll
        fields = '__all__'

        widgets = {
            # 'p': forms.NumberInput(attrs={'class': 'form-control font-vazir-fadigit'}),
            # 'amount': forms.NumberInput(attrs={'type': 'text', 'class': 'form-control font-vazir-fadigit', 'onkeyup': 'javascript:this.value=itpro(this.value);'}),
            # 'date': forms.DateInput(attrs={'type': 'data-jdp', 'class': 'form-control font-vazir-fadigit'}),
        }
