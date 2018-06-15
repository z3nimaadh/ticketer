from django import forms
from .models import Subdomain

class SendData(forms.ModelForm):
    class Meta:
        model = Subdomain
        fields = ('subdomain', 'username', 'token', 'requester_ids', 'subjects', 'descriptions' )