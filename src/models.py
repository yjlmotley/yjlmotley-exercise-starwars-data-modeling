from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from eralchemy2 import render_er
import datetime

Base = declarative_base()


class Planet(Base): 
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    character_pic = Column(String(512), nullable=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    character_pic = Column(String(512), nullable=True)

class FavoriteLike(Base): 
    __tablename__ = 'favorite_like'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Register(Base): 
    __tablename__ = 'register'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    username = Column(String(25), unique=True)
    email = Column(String(250), unique=True)
    password = Column(String(50), nullable=False)

class LogIn(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=datetime.datetime.now())
    success = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    register_id = Column(Integer, ForeignKey('register.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')