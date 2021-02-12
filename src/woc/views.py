from django.views.generic import TemplateView
from rest_framework.views import APIView
from decouple import config
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect
import requests
from django.contrib.auth.models import User
from django.contrib.auth import login

class VueView(TemplateView):
    template_name = 'index.html'

class LoginView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        SCOPE = 'profile+email'
        CLIENT_ID = config('GOOGLE_OAUTH2_KEY',cast=str)
        CLIENT_SECRET = config('GOOGLE_OAUTH2_SECRET',cast=str)
        FRONTEND_URL=config('FRONTEND_URL',cast=str)
        REDIRECT_URI = config('REDIRECT_URL',cast=str)
        if not request.GET.get('code'):
            auth_uri = ('https://accounts.google.com/o/oauth2/v2/auth?response_type=code'
                        '&client_id={}&redirect_uri={}&scope={}').format(CLIENT_ID, REDIRECT_URI, SCOPE)
            return redirect(auth_uri)

        else:
            auth_code = request.GET.get('code')
            data = {'code': auth_code,
                    'client_id': CLIENT_ID,
                    'client_secret': CLIENT_SECRET,
                    'redirect_uri': REDIRECT_URI,
                    'grant_type': 'authorization_code'}
            token = requests.post('https://oauth2.googleapis.com/token', data=data)
            resp = requests.post('https://oauth2.googleapis.com/tokeninfo', data=token)

            data = resp.json()
        user = User.objects.filter(email=data['email']).first()
        if user is None:
            user = User.objects.create_user(
                email=data["email"], username=data["name"])
        login(request, user)
        return redirect(FRONTEND_URL+'/dashboard')

