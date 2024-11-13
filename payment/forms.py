from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):

    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'full name'}), required=True)
    shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email adress'}), required=True)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'address1'}), required=True)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'address2'}), required=True)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=True)
    shipping_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), required=False)
    shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}), required=False)
    shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'country'}), required=True)
    
    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country']
    
        exclude = ['user',]
    
class PaymentForm(forms.Form):
    cart_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'name on cart'}), required=True)
    cart_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cart name'}), required=True)
    cart_cvv = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CVV code'}), required=True)
    cart_ext_date = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'date'}), required=True)
    cart_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'adress1'}), required=True)
    cart_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'adress2'}), required=True)
    cart_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'city'}), required=True)
    cart_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'state'}), required=True)
    cart_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'zip code'}), required=True)
    cart_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'country'}), required=True)

    
    
 