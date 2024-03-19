from django import forms

from regular_exam.cars.models import Car


class BaseClassCarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ('owner',)

        widgets = {
            'image_url': forms.URLInput(
                attrs={'placeholder': "https://..."}
            )
        }
        error_messages = {
            'image_url': {
                'unique': "This image URL is already in use! Provide a new one.",
            }
        }


class CarForm(BaseClassCarForm):
    pass


class DeleteCarForm(BaseClassCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

