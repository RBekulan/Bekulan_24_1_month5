"""AAfisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from movie_app.views import *
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:pk>/', DirectorDetailAPIView.as_view()),
    path('api/v1/movies/', MovieListAPIView.as_view()),
    path('api/v1/movies/<int:pk>/', MovieDetailAPIView.as_view()),
    path('api/v1/reviews/', ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('api/v1/movies/reviews/', ReviewMoviesView.as_view()),
    path('api/v1/users/registration/', RegistrationAPIView.as_view()),
    path('api/v1/users/confirm/', ConfirmUserAPIView.as_view()),
    path('api/v1/users/authorization/', AuthorizationAPIView.as_view()),
]




# from django.contrib import admin
# from django.urls import path
# from movie_app import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/movies/', views.movies_view),
#     path('api/v1/director/', views.director_view),
#     path('api/v1/reviews/', views.reviews_view),
#     path('api/v1/reviews/<int:id>/', views.review_detail_view),
#     path('api/v1/movies/<int:id>/', views.movies_detail_view),
#     path('api/v1/director/<int:id>/', views.director_detail_view),
#     path('api/v1/movies/reviews/', views.review_movies_view),
# ]
