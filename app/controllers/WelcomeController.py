"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller

from app.models.Category import Category

class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def index(self, view: View):
        return view.render("welcome")

    def about(self, view: View):
        return view.render("about")
    
    def docs(self, view: View):
        return view.render("docs")
    
    def categories(self):
        categories = Category.where("status", "published").get()  # select * from categories where status = 'draft';
        return categories