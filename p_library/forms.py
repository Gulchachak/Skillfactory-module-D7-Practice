from django import forms  
from p_library.models import Author, Book, Friend, UserProfile
from django.forms import formset_factory

class ProfileCreationForm(forms.ModelForm):  
  
    class Meta:  
        model = UserProfile  
        fields = ['age']

class AuthorForm(forms.ModelForm):  
  
    full_name = forms.CharField(widget=forms.TextInput)  
  
    class Meta:  
        model = Author  
        fields = '__all__'

AuthorFormSet = formset_factory(AuthorForm)

class BookForm(forms.ModelForm):  
    class Meta:  
        model = Book  
        fields = '__all__'

BookFormSet = formset_factory(BookForm)

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = '__all__'