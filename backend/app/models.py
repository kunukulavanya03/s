from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    posts = relationship('Post', back_populates='author')
    designs = relationship('Design', back_populates='author')
    comments = relationship('Comment', back_populates='author')

    def __repr__(self):
        return f'User(id={self.id}, username={self.username}, email={self.email})'


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    author = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content})'


class Design(Base):
    __tablename__ = 'designs'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    author = relationship('User', back_populates='designs')

    def __repr__(self):
        return f'Design(id={self.id}, name={self.name}, description={self.description})'


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    post = relationship('Post', back_populates='comments')
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    author = relationship('User', back_populates='comments')

    def __repr__(self):
        return f'Comment(id={self.id}, content={self.content})'
