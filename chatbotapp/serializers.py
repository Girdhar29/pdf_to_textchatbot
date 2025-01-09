from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    
    password2= serializers.CharField(style={'input_type':'password'}, write_only = True)
    class Meta:
       
        model = User
        fields = ('name', 'email', 'password','password2','tc')
        extra_kwagrs={
            'password2':{'write_only':True},
            'tc':{'write_only':True}
            }        
        

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        # print(password2,password)
        # print(password2!=password)
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match.'}) 
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ('email', 'password')
        