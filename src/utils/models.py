# Python imports
from typing import Optional

# Lib imports
from sqlmodel import Field, Session, SQLModel, create_engine

# Application imports



class User(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    name: str
    password: str
    email: Optional[str] = None


# NOTE: for sake of example we create an admin user with no password set.
user   = User(name = "Admin", password = "", email = "admin@domain.com")
engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(user)
    session.commit()
