# apps/user/tests.py
from django.contrib.auth.hashers import make_password

from rest_framework import status
from django.test import TestCase
from apps.user.models import User

# Model Test
class TestUser(TestCase):
    '''
        user app의 model test
    '''
    def setUp(self):
        self.user = User(
            id       = 1,
            username = "codestates",
            password = make_password("123"),
            name     = "aaa",
            email    = "aaa@gmail.com",
        )
        self.user.save()
        

    # 회원가입
    def test_register_success(self):
        
        self.user_data = {
            "username"      : "codestates1",
            "password"      : "111222333",
            "password_check": "111222333",
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            }

        self.register_url = "/api/users/sign-up/"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # 회원가입 중복아이디 체크 실패
    def test_register_id_ckeck_fail(self):
        
        self.user_data = {
            "username"      : "codestates", # 중복아이디
            "password"      : "111222333",
            "password_check": "111222333",
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            }

        self.register_url = "/api/users/sign-up/"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    # 회원가입시 패스워드 확인 실패
    def test_register_password_check_fail(self):
        
        self.user_data = {
            "username"      : "codestates112",
            "password"      : "111222333",
            "password_check": "111111111", # 패스워드 확인 오류
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            }

        self.register_url = "/api/users/sign-up/"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
