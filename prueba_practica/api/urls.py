from django.urls import path

from .views import MoviesView, SearchView, TopView

urlpatterns = [
    path('movies/', MoviesView.as_view(), name = 'movies'),
    path('movies/<str:id>', MoviesView.as_view(), name = 'movie-detail'),
    path('search/', SearchView.as_view(), name = 'search'),
    path('top/', TopView.as_view(), name= 'top')
]
