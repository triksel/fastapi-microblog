from core.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey

class Post(Base):
    __tablename__ = 'microblog_post'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey('user.id'))
    user_id = relationship('User')