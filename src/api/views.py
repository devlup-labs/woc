from django.middleware import csrf
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password

import requests
from woc.settings import SOCIAL_AUTH_GOOGLE_OAUTH2_KEY as CLIENT_ID
from woc.settings import SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET as CLIENT_SECRET
from woc.settings import LOGIN_URL as REDIRECT_URI
from woc.settings import FRONTEND_URL
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        SCOPE = 'profile+email'
        auth_uri = ('https://accounts.google.com/o/oauth2/v2/auth?response_type=code'
                    '&client_id={}&redirect_uri={}&scope={}').format(CLIENT_ID, REDIRECT_URI, SCOPE)
        return redirect(auth_uri)


    def post(self, request, *args, **kwargs):
        SCOPE = 'profile+email'

        auth_code = request.data['code']
        print("code",auth_code)
        data = {'code': auth_code,
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'redirect_uri': REDIRECT_URI,
                'grant_type': 'authorization_code'}
        
        token = requests.post('https://oauth2.googleapis.com/token', data=data)
        resp = requests.post('https://oauth2.googleapis.com/tokeninfo', data=token)
        response_data = resp.json()
        print("response_data",response_data)
        user = User.objects.filter(email=response_data['email']).first()
        if user is None:
            user = User.objects.create_user(
                email=response_data["email"], username=response_data["name"],
                password = make_password(BaseUserManager().make_random_password())
                # password="password"
            )
        token = MyTokenObtainPairSerializer.get_token(user)
        response = {}
        response['email'] = user.email
        response['username'] = user.username
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        response['id'] = user.id
        return Response(response, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        return self.get(request, *args, **kwargs)

class CsrfTokenAPIView(APIView):
    permission_classes = (AllowAny,)

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        token = csrf.get_token(request)
        return Response({"csrftoken": token}, status=status.HTTP_200_OK)
