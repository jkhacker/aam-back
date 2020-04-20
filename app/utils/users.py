from app.settings import Session, PWDContext
from app.auth.orm_models import User
from app.utils import randomemail

session = Session()


def create_random_user(is_admin=True):
    password = PWDContext.hash('sasamba')
    return User(email=randomemail(), password=password, is_admin=is_admin)