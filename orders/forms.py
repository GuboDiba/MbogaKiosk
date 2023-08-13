from django import forms
from .models import Order


class ordersUploadForm(forms.ModelForm): 
    
    class Meta:
        # defines the model
        model = Order
        # renders all the fields in the form
        fields = "__all__"

        


