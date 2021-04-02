from django import forms

from .models import Product

class ProductCreateForm(forms.ModelForm):
    title = forms.CharField(label='', 
        widget=forms.TextInput(
        attrs={
            'placeholder':'Enter title',
        }
    ))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'my-class second',
                'rows': 15,
                'cols': 80,
                'placeholder':'Enter description'
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    
    # form validation
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     if not 'CFE' in title:
    #         raise forms.ValidationError('This is not a valid title')
    #     return title

class RawProductForm(forms.Form):
    title = forms.CharField(label='', 
        widget=forms.TextInput(
        attrs={
            'placeholder':'Enter title',
        }
    ))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'my-class second',
                'rows': 15,
                'cols': 80,
                'placeholder':'Enter description'
            }
        )
    )
    price = forms.DecimalField(initial=199.99)