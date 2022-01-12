from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request
from app.models.Category import Category


class CategoryController(Controller):
    
    def index(self, response: Response):
        categories = Category.with_("user").with_count("blogs").all()
        return response.json({
            "data": categories.serialize()
        })

    def store(self, request: Request, response: Response):
        data = request.only('name', 'slug', 'status')
        
        data['user_id'] = request.user().id
        
        category = Category.create(data)
        return response.json({
            "data": category.serialize(),
            "message": "Category created successfully!"
        }, 201)
        
    def update(self, id, request: Request, response: Response):
        data = request.only('name', 'slug', 'status')
        data['user_id'] = request.user().id
        category = Category.find(id)
        if not category:
            return response.json({
                "message": "Category not found!"
            }, 404)
            
        category.update(data)
        return response.json({
            "data": category.fresh().serialize(),
            "message": "Category updated successfully!"
        }, 201)
        
    def destroy(self, id, request: Request, response: Response):
        category = Category.find(id)
        if not category:
            return response.json({
                "message": "Category not found!"
            }, 404)
            
        category.delete()
        
        return response.json({
            "message": "Category deleted successfully!"
        }, 201)
