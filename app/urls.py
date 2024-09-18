from django.contrib import admin
from django.urls import path
from genres.views import GenereCreateListView, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

    
    
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenereCreateListView.as_view(), name='genre_create_list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre_detail_view'),

    path('actors/', ActorCreateListView.as_view(), name='actor_create_list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor_detail_view'),

    path('movies/', MovieCreateListView.as_view(), name='movie_create_list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie_detail_view'),

    path('reviews/', ReviewCreateListView.as_view(), name='review_create_list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review_detail_view'),

]
