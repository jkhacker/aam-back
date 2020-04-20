from sqlalchemy import Boolean, Column, Integer, String
from app.settings import PWDContext, Session
from app.settings import Base


session = Session()


class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)

    def verify_password(self, plain_password: str) -> bool:
        return PWDContext.verify(plain_password, self.password)

    def __repr__(self):
        return "<User with id %d and email %s>" % (self.uid, self.email)

    def __str__(self):
        return "User with id %d and email %s" % (self.uid, self.email)


def get_user(username: str):
    query = session.query(User).filter_by(email=username)
    if query.count() == 0:
        return None
    else:
        return query[0]
