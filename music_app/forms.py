from django import forms

from MusicApp.music_app.models import Profile, Album


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def __set_hidden_fields(self):
        for field in self.fields.values():
            # field.widget = forms.HiddenInput()
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()

        return self.instance


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"


class AlbumCreateForm(AlbumBaseForm):
    class Meta:
        model = Album
        fields = "__all__"
        labels = {
            "album_name": "Album name",
            "artist": "Artist",
            "genre": "Genre",
            "description": "Description",
            "image_url": "Image URL",
            "price": "Price",
        }
        # widgets = {
        #     'album_name': forms.TextInput(attrs={'placeholder': 'Album name'}),
        #     'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
        #     'genre': forms.TextInput(attrs={'placeholder': 'Genre'}),
        #     'description': forms.Textarea(attrs={'placeholder': 'Description'}),
        #     'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
        #     'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        # }


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
