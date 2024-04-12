
from .models import Product, Wishlist
from django import forms
from .models import User,Profile
from django.contrib.auth.forms import PasswordChangeForm

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    is_dealer = forms.BooleanField(label='Are you a dealer?',required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_dealer']
        help_texts={'username':''}
        labels = {
            'username': 'Username ',
            'email'   : 'Email       ',
            'password': 'Password  ',
           
            
        }
        

    def clean(self):
        cleaned_data = super().clean()
        is_dealer = cleaned_data.get('is_dealer')
        dealer_details = cleaned_data.get('dealer_details')

        # if is_dealer and not dealer_details:
        #     raise forms.ValidationError('Dealer details are required for dealer registration')

        return cleaned_data
    
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity','price', 'image']
        labels = {
            'name'    : 'Name  ',
            'quantity': 'Quantity ',
            'price'   : 'Price ',
            'image'   : 'Image ',
        }



class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = []



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)

        # Customize field labels (optional)
        self.fields['old_password'].label = 'Old Password'
        self.fields['new_password1'].label = 'New Password'
        self.fields['new_password2'].label = 'Confirm New Password'
