from django import forms
from .models import Product, Category, Genre


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        genres = Genre.objects.all()
        friendly_cat_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_genre_names = [(g.id, g.get_friendly_name()) for g in genres]

        self.fields['category'].choices = friendly_cat_names
        self.fields['genre'].choices = friendly_genre_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
