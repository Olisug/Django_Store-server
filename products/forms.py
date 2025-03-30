from django import forms
from products.models import Product


class AddProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4,
                                                 'cols': 15}),
        }

    def clean_image(self):
        image = self.cleaned_data['image']
        return image


class EditProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4,
                                                 'cols': 15}),
        }

    def clean_image(self):
        image = self.cleaned_data['image']
        return image
