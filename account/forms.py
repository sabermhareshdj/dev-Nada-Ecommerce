# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# from django import forms


# class CreateUserForm(UserCreationForm):

#     class Meta:

#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super(CreateUserForm, self).__init__(*args, **kwargs)


#     # Email validation

#     def clean_email(self):

#         email = self.cleaned_data.get("email")

#         if User.objects.filter(email=email).exists():

#             raise forms.ValidationError('This email is invalid')
        
#         if len(email >= 350):

#             raise forms.ValidationError('Your email is too long')
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))
