"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller

from app.models.Category import Category
from app.models.User import User

class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def index(self, view: View):
        users = User.with_('categories').all()
        categories = Category.all()
        
        return view.render('welcome', {
            'users': users,
            'categories': categories,
        })

    def about(self, view: View):
        return view.render("about")
    
    def docs(self, view: View):
        return view.render("docs")
    
    def categories(self):
        categories = Category.where("status", "published").get()  # select * from categories where status = 'draft';
        return categories