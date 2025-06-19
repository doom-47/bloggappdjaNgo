from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                              
        try:
            user = serializer.save() 
            return Response({
                'message': 'User registered successfully!',
                'username': user.username,
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                'message': f'An unexpected server error occurred: {str(e)}',
                'data': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
            
class LoginView(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = serializer.validated_data['user']
            
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'message': 'Login successful!',
                'access': access_token,
                'refresh': refresh_token,
                'username': user.username,
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'message': f'An unexpected server error occurred: {str(e)}',
                'data': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)