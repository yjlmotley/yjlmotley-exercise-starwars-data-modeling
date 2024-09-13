from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base, relationship
from eralchemy2 import render_er
import datetime

Base = declarative_base()


class Planet(Base): 
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500))
    character_pic = Column(String(512))

    favorites = relationship('Favorite', backref='planet')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500))
    character_pic = Column(String(512))

    favorites = relationship('Favorite', backref='character')

class Favorite(Base): 
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=datetime.datetime.now())
    success = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=True, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(50), nullable=False)

    favorites = relationship('Favorite', backref='user')
    logins = relationship('Login', backref='user')


    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email
        }


## Draw from SQLAlchemy base
render_er(Base, 'diagram_v2.png')
