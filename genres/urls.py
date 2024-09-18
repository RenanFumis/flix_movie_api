from django.urls import path
from . import views # isso é uma importação relativa, que importa o módulo views do pacote atual

urlpatterns = [
    path('genres/', views.GenereCreateListView.as_view(), name='genre_create_list'),

    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre_detail_view'),
]