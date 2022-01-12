""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, belongs_to_many


class Category(Model):
    """Category Model"""

    __fillable__ = [
        "name",
        "slug",
        "status",
        "user_id",
    ]

    @belongs_to('user_id', 'id')
    def user(self):
        from app.models.User import User
        return User
    
    @belongs_to_many('category_id', 'blog_id', 'id', 'id')
    def blogs(self):
        from app.models.Blog import Blog
        return Blog