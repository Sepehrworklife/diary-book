from django.shortcuts import render
from django.http.request import HttpRequest
from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    password: str
    id: int = 0


class Users:
    """Fake user database as class"""

    ## Some default users as initial
    default_user01 = User("sarina", "sarina@gmail.com", "123")
    default_user02 = User("sepehr", "sepehr@gmail.com", "456")

    def __init__(self) -> None:
        """Initial data"""
        self.users: list[User] = [self.default_user01, self.default_user02]

    def create(self, user: User) -> User:
        """Add one user to the users list

        Args:
            user (User): Dict of user information

        Returns:
            User: user that added to users list
        """
        user["id"] = self.count() + 1
        self.users.append(user)
        return user

    def get(self, email: str) -> User | bool:
        """Get user with his email from users list

        Args:
            email (str): user email

        Returns:
            User | bool: If found return user if not return false
        """
        for user in self.users:
            if user.get("email") == email:
                return user
        return False

    def delete(self, id: int) -> bool:
        """Delete user with specific id

        Args:
            id (int): user id that want to be deleted

        Returns:
            bool: If user deleted True if not False
        """
        for user in self.users:
            if user.get("id") == id:
                self.users.remove(user)
                return True
        return False

    def get_all(self):
        """Get users list

        Returns:
            _type_: all of the users
        """
        return self.users

    def count(self) -> int:
        """How many users do we have?

        Returns:
            int: users count
        """
        return len(self.users)


def login(request: HttpRequest) -> render:
    return render(request, "auth/login.html")


def register(request: HttpRequest) -> render:
    return render(request, "auth/register.html")
