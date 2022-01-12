""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many, belongs_to


class Blog(Model):
    """Blog Model"""
    __fillable__ = [
        "title",
        "slug",
        "excerpt",
        "content",
        "user_id",
        "status"
    ]
    
    @belongs_to('user_id', 'id')
    def user(self):
        from app.models.User import User
        return User
    
    @belongs_to_many('blog_id', 'category_id', 'id', 'id')
    def categories(self):
        from app.models.Category import Category
        return Category
    
