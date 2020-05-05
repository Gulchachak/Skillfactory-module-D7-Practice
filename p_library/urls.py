from django.contrib import admin  
from django.urls import path  
from .views import AuthorEdit, AuthorList, books_list, redactions, author_create_many, books_authors_create_many, FriendCreate, FriendList, index, RegisterView, CreateUserProfile 
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.conf import settings
from allauth.account.views import login, logout
  
app_name = 'p_library' 

urlpatterns = [ 
	path('', index, name='index'),
	path('my_library/', books_list, name='books_list'),
	path('redactions/', redactions, name='redactions'),
#    path('index/book_increment/', views.book_increment),
#    path('index/book_decrement/', views.book_decrement), 
	path('author/create', AuthorEdit.as_view(), name='author_create'),  
	path('authors', AuthorList.as_view(), name='author_list'),
	path('author/create_many', author_create_many, name='author_create_many'),
	path('author_book/create_many', books_authors_create_many, name='books_authors_create_many'),  
	path('friend/create', FriendCreate.as_view(), name='friend_create'),  
	path('friends', FriendList.as_view(), name='friend_list'),
	path('login/', login, name='login'),
	path('logout/', logout, name='logout'),
	path('register/', RegisterView.as_view(template_name='register.html',success_url=reverse_lazy('p_library:profile-create')), name='register'),  
	path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)