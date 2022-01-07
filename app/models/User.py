"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates
from masonite.api.authentication import AuthenticatesTokens

class User(Model, SoftDeletesMixin, Authenticates, AuthenticatesTokens):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __hidden__ = ["password"]
    __auth__ = "email"
