from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import MovieSerializer, NoIDMovieSerializer
from .dao.queries import *

# Create your views here.
class MoviesView(APIView):
    
    def get(self, request, id=None):
        if id:
            movie = get_movie(id)
            if movie:
                serializer = MovieSerializer(movie)
                return Response(serializer.data)
            else:
                return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = MovieSerializer(get_movie_list(), many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            movie = serializer.data
            movie = create_movie(movie)
            return Response(movie, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        serializer = NoIDMovieSerializer(data=request.data)
        if serializer.is_valid():
            movie = serializer.data
            modified_movie = modify_movie(movie, id)

            return Response({'message': modified_movie}) if modified_movie else Response({'message': f'{id} not found'}, status = status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, id):
        message = remove_movie(id)
        return Response({'message': message}) if message else Response({'message': 'No such movie'}, status = status.HTTP_404_NOT_FOUND)
    

class SearchView(APIView):
    def get(self, request):
        q = request.query_params.get('q')
        s =  request.query_params.get('s')
        o =  request.query_params.get('o')
        if q:
            if not s or not o:
                serializer = MovieSerializer(get_filtered_movie_list(q), many = True)
                return Response(serializer.data)
            else:
                serializer = MovieSerializer(get_filtered_sorted_movie_list(q, s, o), many = True)
                return Response(serializer.data)
        else:
            return Response({'message': 'A query is necessary'}, status = status.HTTP_400_BAD_REQUEST)
        
class TopView(APIView):
    def get(self, request):
        serializer = MovieSerializer(get_top_movies(), many = True)
        return Response(serializer.data)