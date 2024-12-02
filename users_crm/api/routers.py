from api.users import router as router_users
from api.auth import router as router_auth

all_routers = [
    router_users,
    router_auth,
]
