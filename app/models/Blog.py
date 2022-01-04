""" User Model """

from masoniteorm.models import Model


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
    
    