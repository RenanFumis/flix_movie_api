from django.contrib import admin
from django.urls import path
from genres.views import GenereCreateListView, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView

    
    
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenereCreateListView.as_view(), name='genre_create_list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre_detail_view'),

    path('actors/', ActorCreateListView.as_view(), name='actor_create_list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor_detail_view'),

]
