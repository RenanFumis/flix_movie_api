from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    def get_rate(self, obj):
        reviews = obj.reviews.all()

        if reviews:
            sum_reviews = 0

            for review in reviews:
                sum_reviews += review.stars
            
            reviews_count = reviews.count()
            rate = round(sum_reviews / reviews_count, 1)
            
            return rate

        return None


        # Implementação do método get_rate
    class Meta:
        model = Movie
        fields = '__all__'
    
    # Toda a validação de dados feitas no serializer são feitas no método validate_<nome_do_campo>
    def validate_release_date(self, value):
        if value.year < 1895:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1895, o ano do primeiro filme.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 300:
            raise serializers.ValidationError('O resumo não pode ter mais de 300 caracteres.')
        return value
