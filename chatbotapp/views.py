from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from chatbotapp.serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from chatbotapp.utils import get_chatbot_response
from django.contrib.auth import authenticate

# Helper function to generate tokens
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
   
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            tokens = get_tokens_for_user(user)
            return Response({'tokens':tokens,'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
   
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)

            if user is not None:
                
                tokens = get_tokens_for_user(user)
                return Response({
                    'msg': 'Login Successful',
                    'tokens': tokens
                }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    

class ChatbotView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_input = request.data.get('message', None)
        # print
        if user_input:
            bot_response = get_chatbot_response(user_input)
            return Response({'response': bot_response}, status=status.HTTP_200_OK)
        return Response({'error': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)





























