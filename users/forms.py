from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'birth_date', 'email']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ContactForm(forms.Form):
    # from_email = forms.EmailField(label='Укажите Ваш Email',
    #                               required=True)
    subject = forms.CharField(label='Тема',
                              required=True)
    message = forms.CharField(label='Сообщение',
                              widget=forms.Textarea,
                              required=True)
