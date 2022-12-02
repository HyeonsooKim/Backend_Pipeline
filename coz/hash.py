import hashlib
from cryptography.fernet import Fernet
# from django.conf import settings
import os
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

ENCRYPT_KEY = env('ENCRYPT_KEY')
SALT = env('SALT')

def hashing_userid(id):
    return hashlib.sha256((f"{id}"+SALT).encode('ascii')).hexdigest()

def encrypt_data(data):
    # # 6개월 또는 12개월에 1번씩 업데이트
    # key = Fernet.generate_key()
    # print(f"대칭키:{key}")

    key = ENCRYPT_KEY.encode('ascii')
    fernet = Fernet(key)
    encrypt_str = fernet.encrypt(f"{data}".encode('ascii'))

    return encrypt_str

def decrypt_data(encrypted_str):
    key = ENCRYPT_KEY.encode('ascii')
    fernet = Fernet(key)
    decrypt_str = fernet.decrypt(encrypted_str)

    return decrypt_str
