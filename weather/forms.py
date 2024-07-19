from django import forms


class ForecastForm(forms.Form):
    city = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
        'class': 'form-control top-spacing-input',
        'id': 'select_city',
        'placeholder': 'Введите город',
        'title': 'Введите город в это поле.',
        'data-api-key': 'ebf5f41483211937312a3638eccb7f9a5c26b89c'
        }),
        required=True,
        label=""
    )
