from django import forms

from .models import User

class RegisterForm(forms.ModelForm ):

    email = forms.EmailField( max_length= 255 , required=True , widget= forms.TextInput(
        attrs={'class': 'form-control form-control-lg border-btn color-bt field '}
    ) )
    first_name = forms.CharField( max_length= 100 , required=True , widget= forms.TextInput(
        attrs={'class': 'form-control form-control-lg border-btn color-bt field text-capitalize'}
    ) )
    last_name = forms.CharField( max_length= 50 , required=True , widget= forms.TextInput(
        attrs={'class': 'form-control form-control-lg border-btn color-bt field text-capitalize'}
    ) )
    password = forms.CharField( max_length= 50 , required=True , widget= forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg border-btn color-bt field'}
    ) )  

    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'email' , 'password' ]


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.username = "{}{}".format(self.cleaned_data["first_name"], self.cleaned_data["last_name"][:2])
        if commit:
            user.save()
        return user

class LoginForm(forms.ModelForm):
    email = forms.EmailField( max_length= 255 , required=True , widget= forms.TextInput(
        attrs={'class': 'form-control form-control-lg border-btn color-bt field '}
    ) )

    password = forms.CharField( max_length= 50 , required=True , widget= forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg border-btn color-bt field'}
    ) )
    
    class Meta:
        model = User
        fields = [ 'email' , 'password' ]
