from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from eralchemy2 import render_er

Base = declarative_base()


class Planets(Base): 
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    character_pic = Column(String(512), nullable=True)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    character_pic = Column(String(512), nullable=True)

class Favorites(Base): 
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    character_id = Column(String(50), ForeignKey('characters.id'))
    planet_id = Column(String(50), ForeignKey('planets.id'))

class Register(Base): 
    __tablename__ = 'register'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    username = Column(String(25), unique=True)
    email = Column(String(250), unique=True)
    password = Column(String(50), nullable=False)
    confirm_password = Column(String(50), ForeignKey('register.password'))

class LogIn(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), ForeignKey('register.id'))
    password = Column(String(50), ForeignKey('register.id'))

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), ForeignKey('register.id'))
    username = Column(String(25), ForeignKey('register.id'))
    # username = Column(String(25), ForeignKey('login.username'))
    email = Column(String(250), ForeignKey('register.id'))
    login_id = Column(String(50), ForeignKey('login.id'))
    favorite_id = Column(String(50), ForeignKey('favorites.id'))
    character_id = Column(String(50), ForeignKey('characters.id'))
    planet_id = Column(String(50), ForeignKey('planets.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')