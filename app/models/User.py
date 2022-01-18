"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates
from masonite.api.authentication import AuthenticatesTokens

from masoniteorm.relationships import has_many

class User(Model, SoftDeletesMixin, Authenticates, AuthenticatesTokens):
    """User Model."""
    
    __fillable__ = ["name", "email", "password"]
    
    __hidden__ = ["password"]
    
    __auth__ = "email"
    
    @has_many('id', 'user_id')
    def categories(self):
        from app.models.Category import Category
        return Category

    @has_many('id', 'user_id')
    def blogs(self):
        from app.models.Blog import Blog
        return Blog
