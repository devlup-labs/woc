from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import requests
from rest_framework.permissions import IsAuthenticated


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.first_name+'_'+user.last_name
        token['email'] = user.email
        # token['isProfileCompleted'] = user.isProfileCompleted
        return token
