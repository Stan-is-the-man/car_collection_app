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

    widgets = {
        'username': forms.TextInput(attrs={'placeholder': 'Username'}),

        'email': forms.EmailInput(attrs={'placeholder': 'Email'}),

        'age': forms.NumberInput(attrs={'placeholder': 'Age'}),

        'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),

        'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),

        'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),

        'profile_picture': forms.URLInput(attrs={'placeholder': 'Profile Picture'}),
    }


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

    widgets = {
        'type': forms.TextInput(attrs={'placeholder': 'Type'}),

        'model': forms.TextInput(attrs={'placeholder': 'Model'}),

        'year': forms.NumberInput(attrs={'placeholder': 'Year'}),

        'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),

        'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
    }


class DeleteCarForm(forms.ModelForm):
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

    widgets = {
        'type': forms.TextInput(attrs={'placeholder': 'Type'}),

        'model': forms.TextInput(attrs={'placeholder': 'Model'}),
        # NUmberINput            !!!!!!!!!!!!!!!!!!!!!!!!!!
        'year': forms.NumberInput(attrs={'placeholder': 'Year'}),

        'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),

        'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
    }
