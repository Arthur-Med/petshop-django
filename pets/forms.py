from django import forms
from .models import Pet, Cliente

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['cliente', 'nome', 'especie', 'raca', 'peso']
        
        # Injetando o visual do Bootstrap nos campos
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Bidu'}),
            'especie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Cachorro, Gato'}),
            'raca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Poodle'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Matheus Silva'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
        }