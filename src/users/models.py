from django.db import models
from dataclasses import dataclass

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=65)


class UsersORM:
    @dataclass
    class Schema:
        name: str
        email: str
        password: str

    def insert(self, user: Schema):
        """Insert a new record in the database

        Args:
            user (Schema): Users Database
            user.name (str)
            user.email (str)
            password.email (str)
        """
        if self.get(user.get("email")):
            raise Exception("Email already exists.")
        instance = Users()
        instance.email = user.get("email")
        instance.name = user.get("name")
        instance.password = user.get("password")
        instance.save()

    def get(self, email: str) -> bool | Users:
        """Fetch user with email

        Args:
            email (str): User Email

        Returns:
            bool|Users: If true returns user information
        """
        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            user = False
        return user
