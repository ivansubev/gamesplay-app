from django import forms
from django.forms import ModelForm, CharField, FloatField

from gamesplay_app.core.models import Profile, GameModel


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }


class GameForm(ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


class DeleteGameForm(ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = GameModel
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'readonly': 'true'}),
            'category': forms.TextInput(attrs={'readonly': 'true'}),
            'rating': forms.TextInput(attrs={'readonly': 'true'}),
            'max_level': forms.TextInput(attrs={'readonly': 'true'}),
            'image_url': forms.TextInput(attrs={'readonly': 'true'}),
            'summary': forms.TextInput(attrs={'readonly': 'true'})
        }


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(ModelForm):
    def save(self, commit=True):
        games = GameModel.objects.all()
        games.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = []
