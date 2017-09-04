from apistar import Route, Include
from .views import create_user, users_list


user_routes = [
    Route('', "GET", users_list),
    Route('', "POST", create_user)
]