from masonite.controllers import Controller
from masonite.facades.Hash import Hash
from app.models.User import User
from masonite.request import Request
from masonite.response import Response
from app.validation.UserRule import UserRule

class UsersController(Controller):
    
    def index(self, response: Response):
        users = User.all()
        return response.json({
            "data": users.serialize()
        })

    def store(self, request: Request, response: Response):
        errors = request.validate(UserRule)
        if errors:
            return response.json({
                "message": "Data validation failed!",
                "errors": errors.all()
            }, 422)
            
        data = request.only('name', 'email', 'password')
        data['password'] = Hash.make(data['password']).decode('utf-8')
        user = User.create(data)
        return response.json({
            "data": user.serialize(),
            "message": "User created successfully!"
        }, 201)
        
    def show(self, id, request: Request, response: Response):
        user = User.find(id)
        if not user:
            return response.json({
                "message": "User not found!"
            }, 404)
            
        return response.json({
            "data": user.serialize()
        })
        
    def update(self, id, request: Request, response: Response):
        
        errors = request.validate(UserRule)
        if errors:
            return response.json({
                "message": "Data validation failed!",
                "errors": errors.all()
            }, 422)
            
        data = request.only('name', 'email')
        
        user = User.find(id)
        if not user:
            return response.json({
                "message": "User not found!"
            }, 404)
            
        if request.input('password'):
            data['password'] = Hash.make(request.input('password')).decode('utf-8')
            
        user.update(data)
        return response.json({
            "data": user.serialize(),
            "message": "User updated successfully!"
        }, 201)
        
    def destroy(self, id, request: Request, response: Response):
        user = User.find(id)
        if not user:
            return response.json({
                "message": "User not found!"
            }, 404)
            
        user.delete()
        
        return response.json({
            "message": "User deleted successfully!"
        }, 201)