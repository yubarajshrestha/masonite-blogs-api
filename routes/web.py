from masonite.routes import Route

ROUTES = [
    Route.get('/test', 'WelcomeController@test'),
    Route.get("/", "WelcomeController@show")
]
