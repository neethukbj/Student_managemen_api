from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.ListCreateAPIView):
    queryset= User.objects.all()
    serializer_class=RegisterSerializer


class LoginView(generics.GenericAPIView):
	
	serializer_class=LoginSerializer
	

	def post(self,request):
                # logger.info(f"Request data: {request.data}")  # Log the incoming request data
                try:
                        data = request.data
                        serializer = self.get_serializer(data=data)
                        serializer.is_valid(raise_exception=True)
            # If valid, get the JWT token
                        response = serializer.get_jwt_token(serializer.validated_data)
                        return Response(response, status=status.HTTP_200_OK)
        
                except serializers.ValidationError as e:
                        # logger.error(f"Validation error: {e.detail}")  # Log the validation errors
                        return Response({"data": e.detail, "message": "Invalid credentials!"}, status=status.HTTP_400_BAD_REQUEST)

                except Exception as e:
                        # logger.error(f"Exception: {str(e)}")  # Log any other exceptions
                        return Response({"data": {}, "message": "Something went wrong..!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

# class LoginView(generics.GenericAPIView):
#     #queryset=User.objects.all()
#     serializer_class= LoginSerializer

#     def post(self,request):

#         try:
#             data=request.data
#             serializer = self.get_serializer(data=data)
#             serializer.is_valid(raise_exception=True)
#             response=serializer.get_jwt_token(serializer.validated_data)
#             return Response(response)
#         # expect serializers.ValidationError as e:
#         #     return Response({"data":e.detail,"message":"Invalid credentails.."})
              
#         except Exception as e:
#             return Response({"message":"Something wrong!"})