from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login

User = get_user_model()
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        email = attrs.get('email')
        if email:
            if User.objects.filter(email=email).exists():
                msg = {'detail': 'User is already associated with another user. Try a new one.',
                       'status': False}
                raise serializers.ValidationError(msg)
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            if User.objects.filter(email=email).exists():
                user = authenticate(request=self.context.get('request'), email=email, password=password)
                if user is None:
                    raise serializers.ValidationError('Authentication failed, Please try again')
                try:
                    payload = JWT_PAYLOAD_HANDLER(user)
                    jwt_token = JWT_ENCODE_HANDLER(payload)
                    update_last_login(None, user)
                except:
                    raise serializers.ValidationError('Authentication failed, Please try again')
            else:
                raise serializers.ValidationError('There is no user with this email')
        else:
            raise serializers.ValidationError('Email or Password has not been entered')

        return {'email': user.email,
                'token': jwt_token}
