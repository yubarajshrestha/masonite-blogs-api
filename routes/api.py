from masonite.routes import Route

ROUTES = [
    # Users Route
    Route.get('/users', 'UsersController@index'),
    Route.get('/users/@id:int', 'UsersController@show'),
    Route.post('/users', 'UsersController@store'),
    Route.put('/users/@id:int', 'UsersController@update'),
    Route.delete('/users/@id:int', 'UsersController@destroy'),
    
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