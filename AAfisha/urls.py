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
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from movie_app.views import *
from user.views import *

from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

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
