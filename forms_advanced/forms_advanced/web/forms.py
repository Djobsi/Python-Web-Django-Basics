from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelform_factory

from forms_advanced.web.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    # def clean(self, *args, **kwargs):
    #     cleaned_data = super().clean(*args, **kwargs)
    #     print(cleaned_data)
    #     return cleaned_data

    def __init__(self, *args, **kwargs):
        if "user" in kwargs:
            self.user = kwargs.pop("user")

        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user.is_authenticated:
            instance.created_by = self.user
        instance.save()
        return instance

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@gmail.com'):
            raise ValidationError('Wrong domain')
        return email


class ReadOnlyFieldsMixin:
    readonly_fields = ()

    def _mark_readonly_fields(self):
        for field_name in self.readonly_fields:
            self.fields[field_name].widget.attrs["readonly"] = "readonly"
        # for _, field in self.fields.items():
        #     field.widget.attrs["readonly"] = "readonly"


class UpdatePersonForm(ReadOnlyFieldsMixin, PersonForm):
    readonly_fields = ("age", "last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._mark_readonly_fields()


PersonForm2 = modelform_factory(Person, fields="__all__")
