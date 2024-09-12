from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.CharField(max_length = 50)
    name = serializers.CharField(max_length = 50)
    country = serializers.CharField(max_length = 50)
    score = serializers.FloatField()

class NoIDMovieSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 50)
    country = serializers.CharField(max_length = 50)
    score = serializers.FloatField()