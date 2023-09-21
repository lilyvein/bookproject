from django.urls import path
from . import views

app_name = 'booksapp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),  # Home View
    path('country_list/', views.CountryListView.as_view(), name='country_list'),  # Country List View
    path('country_create/', views.CountryCreateView.as_view(), name='country_create'),  # Country List View
    path('country_update/<int:pk>', views.CountryUpdateView.as_view(), name='country_update'),  # Country Update View
    path('country_delete/<int:pk>', views.CountryDeleteView.as_view(), name='country_delete'),  # Country Delete View


    path('language_list/', views.LanguageListView.as_view(), name='language_list'),  # Language List View
    path('language_create/', views.LanguageCreateView.as_view(), name='language_create'),
    path('language_update/ <int:pk>', views.LanguageUpdateView.as_view(), name='language_update'),
    path('language_delete/<int:pk>', views.LanguageDeleteView.as_view(), name='language_delete'),


    path('author_list/', views.AuthorListView.as_view(), name='author_list'),  # Author List View
    path('author_create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('author_update/<int:pk>', views.AuthorUpdateView.as_view(), name='author_update'),
    path('author_detail/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),  # Author detail view
    path('author_delete/<int:pk>', views.AuthorDeleteView.as_view(), name='author_delete'),

    path('book_list/', views.BookListView.as_view(), name='book_list'),  # Book List View
    path('book_create/', views.BookCreateView.as_view(), name='book_create'),
    path('book_update/<int:pk>', views.BookUpdateView.as_view(), name='book_update'),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('book_delete/<int:pk>', views.BookDeleteView.as_view(), name='book_delete'),

]
