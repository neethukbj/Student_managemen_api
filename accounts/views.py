from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response

class RegisterView(generics.ListCreateAPIView):
    queryset= User.objects.all()
    serializer_class=RegisterSerializer

class LoginView(generics.GenericAPIView):
    #queryset=User.objects.all()
    serializer_class= LoginSerializer

    def post(self,request,*args,**kwargs):

        try:
            data=request.data
            serializer = LoginSerializer(data=data)
            if not serializer.is_valid():
                return Response({"data":serializer.errors,"message":"Something went wrong...!"})
        
            response=serializer.get_jwt_token(serializer.validated_data)

            return Response(response)
        except Exception as e:
            return Response({"message":"Something wrong!"})