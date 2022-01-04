from masoniteorm import Factory
from app.models.Category import Category
from app.models.User import User
from masonite.facades.Hash import Hash

def user_factory(faker):
    return {
        'name': faker.name(),
        'email': faker.email(),
        'password': Hash.make("secret").decode("utf-8"),
    }
    
def category_factory(faker):
    name = faker.name()
    slug = name.lower().replace(" ", "-")
    return {
        "name": faker.name(),
        "slug": slug,
    }
    
Factory.register(User, user_factory)
Factory.register(Category, category_factory)