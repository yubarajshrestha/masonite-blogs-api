from masonite.routes import Route
from masonite.api import Api
from masonite.authentication import Auth

ROUTES = [
    Route.get("/", "WelcomeController@index"),
    Route.get('/about', 'WelcomeController@about'),
    Route.get("/docs", "WelcomeController@docs"),
] + Api.routes(auth_route="/api/auth", reauth_route="/api/reauth") + Auth.routes()
