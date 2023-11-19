# Python imports
from typing import Optional
from os import path

# Lib imports
from sqlmodel import Session, create_engine

# Application imports
from .models import SQLModel, User



class DB:
    def __init__(self):
        super(DB, self).__init__()
        
        self.create_engine()

        # NOTE: for sake of example we create an admin user with no password set.
        self.add_user_entry(name = "Admin", password = "", email = "admin@domain.com")

    def create_engine(self):
        db_path     = f"sqlite:///{settings_manager.get_home_config_path()}/database.db"
        self.engine = create_engine(db_path)

        SQLModel.metadata.create_all(self.engine)

    def _add_entry(self, entry):
        with Session(self.engine) as session:
            session.add(entry)
            session.commit()


    def add_user_entry(self, name = None, password = None, email = None):
        if not name or not password or not email: return

        user   = User(name, password, email)
        self._add_entry(user)
