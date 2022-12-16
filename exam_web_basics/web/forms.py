from django import forms

from exam_web_basics.web.models import Profile, Car


class CrateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # labels = {
        #     'first_name': 'First Name',
        #     'last_name': 'Last Name',
        #     'profile_picture': 'Profile Picture',
        #
        # }


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        Car.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'type': 'Type',
            'model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',

        }


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'type': 'Type',
            'model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',

        }


class DeleteCarForm(forms.ModelForm):
    # readonly words in the fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'type': 'Type',
            'model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',

        }
