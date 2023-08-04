import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    username = Column(String(30))
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50), nullable=False, unique=True)

class Follower(Base):
    __tablename__ = 'followers'
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='followers')
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='followers') 
    
class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='post')

class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(2000))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', back_populates='comment')
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='comment')

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(1000))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', back_populates='media')


""" class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {} """

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
