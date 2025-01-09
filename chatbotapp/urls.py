from django.urls import path
from .views import ChatbotView,UserRegistrationView,UserLoginView,get_tokens_for_user
urlpatterns = [
    
    path("register/",UserRegistrationView.as_view(), name = 'register'),
    path("login/",UserLoginView.as_view(), name = 'login'),
    path('chatbot/', ChatbotView.as_view(), name='ChatBot'),
]   


