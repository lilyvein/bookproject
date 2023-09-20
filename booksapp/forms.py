from django import forms
import bookproject.settings
from .models import *


class LanguageCreateForm(forms.ModelForm):
    language = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a new language name',
                                                             'class': 'form-control', 'autofocus': True}))

    class Meta:
        model = Language
        fields = ['language']  # '__all__'


class AuthorCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'
            visible.field.widget.attrs['placeholder'] = visible.field.label

        self.fields['firstname'].widget.attrs['autofocus'] = True
        self.fields['birth'].widget = forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control mb-2'})

    class Meta:
        model = Author
        fields = '__all__'


class BookCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'

        self.fields['title'].widget.attrs['autofocus'] = True  # hiire kursor läheb sellele lahtrile
        self.fields['book_published_year'].widget = forms.widgets.TextInput(attrs={
        'type': 'number',
        'class': 'form-control mb-2',
        'min': 1900,
        'step': 1,
        })

    class Meta:
        model = Book
        fields = '__all__'
