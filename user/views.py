
# Create your views here.
import random
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status


from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, UserLoginSerializer
from .models import UserConfirmation
import random

class RegistrationAPIView(ListAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(is_active=False)
            confirmation = UserConfirmation.objects.create(user=user, code=random.randint(100000, 999999))
            return Response({'status': 'User registered', 'code': confirmation.code}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmUserAPIView(ListAPIView):
    def post(self, request, *args, **kwargs):
        code = request.data.get('code', None)
        confirmation = get_object_or_404(UserConfirmation, code=code)
        user = confirmation.user
        user.is_active = True
        user.save()
        confirmation.delete()
        return Response({'status': 'User activated'}, status=status.HTTP_200_OK)


class AuthorizationAPIView(ListAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

