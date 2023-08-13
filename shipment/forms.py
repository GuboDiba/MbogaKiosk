from django import forms
from .models import Shipment

class ShippingUploadForm(forms.ModelForm): 
    
    class Meta:
        # defines the model
        model = Shipment
        # renders all the fields in the form
        fields = "__all__"

        


