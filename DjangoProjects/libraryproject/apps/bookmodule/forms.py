from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'edition', 'price', 'quantity', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter book title',
                'style': 'width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box;'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Enter author name',
                'style': 'width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box;'
            }),
            'edition': forms.NumberInput(attrs={
                'min': '1',
                'style': 'width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box;'
            }),
            'price': forms.NumberInput(attrs={
                'min': '0',
                'step': '0.01',
                'style': 'width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box;'
            }),
            'quantity': forms.NumberInput(attrs={
                'min': '0',
                'style': 'width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box;'
            }),
            'rating': forms.NumberInput(attrs={
                'min': '1',
                'max': '5',
                'style': 'width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box;'
            }),
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'edition': 'Edition',
            'price': 'Price ($)',
            'quantity': 'Quantity',
            'rating': 'Rating (1-5)',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise forms.ValidationError('Title cannot be empty.')
        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long.')
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author', '').strip()
        if not author:
            raise forms.ValidationError('Author cannot be empty.')
        if len(author) < 2:
            raise forms.ValidationError('Author name must be at least 2 characters long.')
        return author

    def clean_edition(self):
        edition = self.cleaned_data.get('edition')
        if edition is not None and edition < 1:
            raise forms.ValidationError('Edition must be at least 1.')
        return edition

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Price cannot be negative.')
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity < 0:
            raise forms.ValidationError('Quantity cannot be negative.')
        return quantity

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None and (rating < 1 or rating > 5):
            raise forms.ValidationError('Rating must be between 1 and 5.')
        return rating
