from django import forms
from .models import Customer

class customerRegistrationForm (forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    cpassword=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Customer
        fields=[
             'full_name',
             'first_name',
             'username', 
             'email', 
             'password',
             'address',
             'city',
             'state',
             'country',
             'zip_code'
        ]

        def clean(self):

            cleand_data =super.clean()
            password=cleand_data.get("password")
            cpassword=cleand_data.get("cpassword")

            if password and cpassword and password!=cpassword:
                raise forms.ValidationError("Password did not match!")
            
            return cleand_data
