from django.db import models  
from django.contrib.auth.models import User
  
class UserProfile(models.Model):  
  
    age = models.IntegerField()  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
  
class Author(models.Model):  
	full_name = models.CharField('Имя автора', max_length=50)  
	birth_year = models.SmallIntegerField()  
	country = models.CharField(max_length=2)  
  
	def __str__(self):  
		return self.full_name

class Book(models.Model):
	ISBN = models.CharField(max_length=13)  
	title = models.CharField('Название книги', max_length=128)
	description = models.TextField('Описание')  
	year_release = models.SmallIntegerField('Год публикации') 
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	copy_count = models.SmallIntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	redaction = models.ForeignKey('Redaction', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
	book_image = models.ImageField(upload_to="book_images", null=True)

	def __str__(self):
		return self.title
		
class Redaction(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name	

class Friend(models.Model):  
	friend_name = models.CharField(max_length=60) 
	friend_book = models.ForeignKey('Book', on_delete=models.CASCADE) 
  
	def __str__(self):  
		return self.friend_name