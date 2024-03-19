from django import forms

from regular_exam.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']

    widgets = {
        'password': forms.PasswordInput(),
    }
    help_texts = {
        'age': "Age requirement: 21 years and above.",
    }



class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Profile
        fields = ()
