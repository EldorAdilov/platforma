from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, phone_number=None):
        if not username:
            raise ValueError("Foydalanuvchilarning usernamelari bo'sh bo'lishi shart")
        user = self.model(
            username=username,
            phone_number=None
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, phone_number=None):
        if not password:
            raise ValueError('Superuserlar parol yaratishi shart')
        user = self.create_user(
            username=username,
            password=password,
            phone_number=phone_number
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username',
        max_length=150,
        unique=True,
    )

    phone_number = models.CharField(
        verbose_name='phone_number',
        max_length=150,
        unique=True,
        blank=True,
        null=True,
    )
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.is_admin
