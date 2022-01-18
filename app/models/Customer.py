""" Customer Model """

from masoniteorm.models import Model


class Customer(Model):
    """Customer Model"""
    
    __primary_key__ = "customer_id"
    
    __fillable__ = [
        "name",
    ]
