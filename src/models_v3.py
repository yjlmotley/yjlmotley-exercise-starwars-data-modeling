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
    planet_pic = Column(String(512))
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
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id', ondelete='CASCADE'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id', ondelete='CASCADE'), nullable=True)

    def serialize(self):
        return {
            "type": "character" if self.character else "planet",
            "id": self.character.id if self.character else self.planet.id,
            "name": self.character.name if self.character else self.planet.name
        }

class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
    success = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    logins = relationship('Login', backref='user')
    favorites = relationship('Favorite', backref='user')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'favorites': [favorite.serialize() for favorite in self.favorites]
        }


## Draw from SQLAlchemy base
render_er(Base, 'diagram_v3.png')
