from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    type = Column(String)
    answers = relationship('Answer', backref='question')
    trivias = relationship('Trivia', backref='question')
    settings = relationship('Settings', backref='question')


class Answer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    text = Column(String)
    votes = Column(Integer)


class Trivia(Base):
    __tablename__ = 'trivia'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    correct_answer = Column(String)


class Settings(Base):
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    settings = Column(JSONB)
