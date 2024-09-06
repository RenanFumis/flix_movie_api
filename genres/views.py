from rest_framework import generics # Primeiro é os modulos da implementação e depois os de sua autoria
from genres.models import Genre
from genres.serializers import GenreSerializer



class GenereCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


