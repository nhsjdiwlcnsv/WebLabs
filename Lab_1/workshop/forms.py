from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)
from django.contrib.auth import get_user_model

from .models import Order, Service

User = get_user_model()


class CreateServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service_type'].empty_label = 'Unspecified'

    title = forms.CharField(
        label='Name of the service',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name of the service'
        })
    )
    price = forms.FloatField(
        label='Price of the service',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Price of the service'
        })
    )
    description = forms.CharField(
        label='Price of the service',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Description'
        })
    )

    class Meta:
        model = Service
        fields = ['title', 'price', 'service_type', 'slug', 'description']


class CreateOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].empty_label = 'Unspecified'

    # created_by = forms.ChoiceField(
    #     widget=forms.Widget(attrs={
    #         'placeholder': 'Author'
    #     }),
    #     disabled=True,
    # )

    content = forms.Textarea(attrs={
        'rows': 20,
        'cols': 60,
        'class': 'form-control',
        'placeholder': 'Type anything here'
    }),

    class Meta:
        model = Order
        fields = ['created_by', 'service', 'content']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }),
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password')
