from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from uploadfile.models import Uploadfile

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password, file, image_url):
        """
        Creates and saves a User with the given email, file
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model (
            username=username,
            email=self.normalize_email(email),
            password=password,
            file=file,
            image_url=image_url
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        file = Uploadfile.objects.get(pk=1)
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
            file=file,
            image_url=''
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
class CustomUser(AbstractUser):
    email = models.EmailField(
        unique=True,
    )
    file = models.ForeignKey(Uploadfile, on_delete=models.CASCADE)
    image_url = models.URLField()
    objects = MyUserManager()
    # favorite_recipes = models.ManyToManyField('recipes.Recipes', through='favoriterecipe.FavoriteRecipe')
    # user_followings = models.ManyToManyField("self", through='relationships.Relationships')