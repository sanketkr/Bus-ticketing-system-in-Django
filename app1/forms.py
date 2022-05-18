from django.forms import Form, ModelForm, DateField, widgets

from django import forms
from .models import Tickets
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class TicketsForm(forms.ModelForm):
    class Meta:
        model=Tickets#bas yahi krne se hi sara 'Tickets' ka sara attributes aa gaya isme.
        fields=['date_of_travel','source','destination']
        widgets = { 

        'date_of_travel': widgets.DateInput(attrs={'type': 'date'}),
        'source' : widgets.TextInput(attrs={'placeholder': 'Start typing to search'}),
        'destination' : widgets.TextInput(attrs={'placeholder': 'Start typing to search'}),

        }
        # this is just customization of text area, it will be 80 column wide






