from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@index"),
    Route.get('/about', 'WelcomeController@about'),
    Route.get("/docs", "WelcomeController@docs"),
    
    # Blogs Route
    Route.get('/blogs', 'BlogsController@index'),
    Route.get('/blogs/@id:int', 'BlogsController@show'),
    Route.post('/blogs', 'BlogsController@store'),
    Route.put('/blogs/@id:int', 'BlogsController@update'),
    Route.delete('/blogs/@id:int', 'BlogsController@destroy'),
    
    # Categories Route
    Route.get('/categories', 'CategoryController@index'),
    Route.post('/categories', 'CategoryController@store'),
    Route.put('/categories/@id:int', 'CategoryController@update'),
    Route.delete('/categories/@id:int', 'CategoryController@destroy'),
]
