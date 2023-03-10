from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import *
from .models import *


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DirectorValidatorCreate
        return self.serializer_class


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return DirectorValidatorCreate
        return self.serializer_class


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MovieValidatorsCreate
        return self.serializer_class


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return MovieDetailValidatorCreate
        return self.serializer_class


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewMoviesView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from movie_app.models import *
# from movie_app.serializers import *
#
#
# @api_view(['GET'])
# def movies_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# def director_view(request):
#     if request.method == 'GET':
#         director = Director.objects.all()
#         serializer = DirectorSerializer(director, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# def reviews_view(request):
#     if request.method == 'GET':
#         review = Review.objects.all()
#         serializer = ReviewSerializer(review, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# def review_detail_view(request, **kwargs):
#     try:
#         review = Director.objects.get(id=kwargs['id'])
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = DirectorSerializer(review, many=False)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         review.name = request.data.get("name")
#         review.save()
#         return Response(data={'message': 'data received!',
#                               'review': ReviewSerializer(review).data})
#
#
# @api_view(['GET'])
# def movies_detail_view(request, **kwargs):
#     try:
#         movies = Director.objects.get(id=kwargs['id'])
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = DirectorSerializer(movies, many=False)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         movies.name = request.data.get("name")
#         movies.save()
#         return Response(data={'message': 'data received!',
#                               'movies': MovieSerializer(movies).data})
#
#
# @api_view(['GET', 'DELETE', 'PUT'])
# def director_detail_view(request, **kwargs):
#     try:
#         director = Director.objects.get(id=kwargs['id'])
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = DirectorSerializer(director, many=False)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         director.name = request.data.get("name")
#         director.save()
#         return Response(data={'message': 'data received!',
#                               'director': DirectorSerializer(director).data})
#
#
# @api_view(["GET"])
# def review_movies_view(request):
#     if request.method == "GET":
#         movie = Movie.objects.all()
#         serializer = MovieReviewSerializer(movie, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
