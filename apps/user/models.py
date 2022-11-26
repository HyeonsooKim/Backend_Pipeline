# apps/user/models.py
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, name, password, **kwargs):
        if not username:
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have a name')

        user = self.model(
            username=username,
            email=email,
            name=name
        )
        user.is_staff=False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, username, password=None):
        superuser = self.create_user(
            username=username,
            password=password,
            email=email,
            name=name
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False
        )
    email = models.EmailField(
        max_length=30, 
        unique=True, 
        null=False, 
        blank=False
        )
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False
        )
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True
        )
    is_staff = models.BooleanField(
        verbose_name=_('Is staff'),
        default=False
        )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    class Meta:
        db_table = 'user'
