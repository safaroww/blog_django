from dataclasses import field
from distutils.command.clean import clean
from django import forms
from .models import Tag
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title:
            if Tag.objects.filter(title__iexact=title).exists():
                raise ValidationError('Bele bir tag movcuddur!', code='same')