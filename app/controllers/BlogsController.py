import json
from masonite.controllers import Controller
from masoniteorm.query.QueryBuilder import QueryBuilder
from app.models.Blog import Blog
from masonite.request import Request
from masonite.response import Response
from masoniteorm.exceptions import QueryException

from app.validation.BlogRule import BlogRule

class BlogsController(Controller):
    
    def index(self, response: Response):
        blogs = Blog.with_('categories', 'user').all()
        return response.json({
            "data": blogs.serialize()
        })

    def store(self, request: Request, response: Response):
        errors = request.validate(BlogRule)
        if errors:
            return response.json({
                "message": "Data validation failed!",
                "errors": errors.all()
            }, 422)
            
        data = request.only('title', 'slug', 'excerpt', 'content', 'user_id', 'status', 'categories')
        data['categories'] = json.loads(data['categories'])
        data['user_id'] = request.user().id
        try:
            blog = Blog.create(data)
            
            blog_categories = []
            for category_id in data['categories']:
                blog_categories.append({
                    "blog_id": blog.id,
                    "category_id": category_id
                })
            QueryBuilder().table("blog_category").bulk_create(blog_categories)
            
            return response.json({
                "data": blog.serialize(),
                "message": "Blog created successfully!"
            }, 201)
        except QueryException as e:
            return response.json({
                "error": str(e),
                "message": "Unable to store data!"
            }, 422)
        
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
        errors = request.validate(BlogRule)
        if errors:
            return response.json({
                "message": "Data validation failed!",
                "errors": errors.all()
            }, 422)
            
        data = request.only('title', 'slug', 'excerpt', 'content', 'user_id', 'status')
        blog = Blog.find(id)
        if not blog:
            return response.json({
                "message": "Blog not found!"
            }, 404)
        blog.update(data)
        
        QueryBuilder().table("blog_category").where("blog_id", id).delete()
        blog_categories = []
        for category_id in data['categories']:
            blog_categories.append({
                "blog_id": blog.id,
                "category_id": category_id
            })
        QueryBuilder().table("blog_category").bulk_create(blog_categories)
        
        return response.json({
            "data": blog.fresh().serialize(),
            "message": "Blog updated successfully!"
        }, 201)
        
    def destroy(self, id, response: Response):
        blog = Blog.find(id)
        if not blog:
            return response.json({
                "message": "Blog not found!"
            }, 404)
            
        blog.delete()
        
        return response.json({
            "message": "Blog deleted successfully!"
        }, 201)