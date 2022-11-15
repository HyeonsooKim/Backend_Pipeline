# DRF
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import AuthenticationFailed
# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from datetime import date
# Internal
from apps.user.models import User

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )
    password_check = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password', 'password_check']

    def validate(self, attrs):
        """
        회원가입 데이터를 검증합니다.
        1. 아이디 중복 체크
        2. 비밀번호
        """

        if User.objects.filter(username=attrs['username']).exists():
            raise ValidationError({'username', '이미 존재하는 아이디입니다.'})

        if attrs['password'] != attrs['password_check']:
            raise ValidationError({'password', '비밀번호와 비밀번호 확인이 일치하지 않습니다.'})

        attrs['created_at'] = date.today()

        return attrs

    def create(self, validated_data):
        """ validated_data를 받아 유저를 생성한 후 토큰을 반환합니다. """
        password = validated_data.get('password')
        # 유저 생성
        user = User(
            username=validated_data['username'],
            password=password,
            name=validated_data['name'],
            email=validated_data['email'],
        )
        user.set_password(password)
        user.save()

        return user