from masonite.controllers import Controller
from app.models.Blog import Blog
from masonite.request import Request
from masonite.response import Response


class BlogsController(Controller):
    
    
    
    def index(self, response: Response):
        blogs = Blog.all()
        return response.json({
            "data": blogs.serialize()
        })

    def store(self, request: Request, response: Response):
        data = request.only('title', 'slug', 'excerpt', 'content', 'user_id', 'status')
        blog = Blog.create(data)
        return response.json({
            "data": blog.serialize(),
            "message": "Blog created successfully!"
        }, 201)
        
    def show(self, id, request: Request, response: Response):
        blog = Blog.find(id)
        if not blog:
            return response.json({
                "message": "Blog not found!"
            }, 404)
            
        return response.json({
            "data": blog.serialize()
        })
        
    def update(self, id, request: Request, response: Response):
        data = request.only('title', 'slug', 'excerpt', 'content', 'user_id', 'status')
        blog = Blog.find(id)
        if not blog:
            return response.json({
                "message": "Blog not found!"
            }, 404)
            
        blog.update(data)
        return response.json({
            "data": blog.serialize(),
            "message": "Blog updated successfully!"
        }, 201)
        
    def destroy(self, id, request: Request, response: Response):
        blog = Blog.find(id)
        if not blog:
            return response.json({
                "message": "Blog not found!"
            }, 404)
            
        blog.delete()
        
        return response.json({
            "message": "Blog deleted successfully!"
        }, 201)