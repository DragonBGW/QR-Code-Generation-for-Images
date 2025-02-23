from django import forms

class QRCodeForms(forms.Form):
    restaurant_name = forms.CharField(
        max_length=50,
          label='restaurant name',
          widget=forms.TextInput(attrs={
              'class':'form-control',
              'placeholder' : 'Enter Restaurant Name'
          })
          )
    url = forms.URLField(
        max_length=200,
        label='Menu URL',
        widget=forms.URLInput(attrs={
              'class':'form-control',
              'placeholder' : 'Enter URL of your online menu'
          })
        )