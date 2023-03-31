from django import forms

class GroundSearchForm(forms.Form):
    ground_name = forms.CharField(label='Ground Name',
                                  max_length=100,
                                  required=False,
                                  widget=forms.TextInput(attrs={'placeholder': 'Search ground',
                                                                'class': 'form-control'}))