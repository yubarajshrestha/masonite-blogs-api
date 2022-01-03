from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@index"),
    Route.get('/about', 'WelcomeController@about'),
    Route.get("/docs", "WelcomeController@docs"),
]
