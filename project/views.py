from apistar.backends.sqlalchemy_backend import Session
from .models import User
from .schemas import UserSchemas
from apistar import http, Response


def create_user(session: Session, user: UserSchemas):
    print(user)
    user = User(**user)
    session.add(user)
    session.flush()
    return UserSchemas(user)


def users_list(session: Session, name):
    print(name)

    queryset = session.query(User).all()
    return [UserSchemas(user) for user in queryset]
