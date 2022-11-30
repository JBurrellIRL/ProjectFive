from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Format, Genre
from django_summernote.widgets import SummernoteWidget


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
        }

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        formats = Format.objects.all()
        genres = Genre.objects.all()
        friendly_format_names = [
            (f.id, f.get_friendly_name()) for f in formats]
        friendly_genre_names = [(g.id, g.get_friendly_name()) for g in genres]

        self.fields['format'].choices = friendly_format_names
        self.fields['genre'].choices = friendly_genre_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
