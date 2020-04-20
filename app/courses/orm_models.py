from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Interval
from sqlalchemy.orm import relationship

from app.settings import Base
from app.auth.orm_models import User


class Course(Base):
    __tablename__ = 'courses'
    courseid = Column(Integer, primary_key=True, index=True)
    title = Column(String)


class Event(Base):
    __tablename__ = 'events'
    evid = Column(Integer, primary_key=True, index=True)
    modid = Column(Integer, ForeignKey(User.uid))
    scheduled_time = Column(DateTime)
    real_start_time = Column(DateTime)
    compl = Column(Boolean)
    chunk_count = Column(Integer)
    chunk_delta = Column(Interval)

    professor = relationship('User', back_populates="events")


class EventForCourse(Base):
    __tablename__ = 'events_for_course'
    courseid = Column(Integer, ForeignKey(Course.courseid), primary_key=True, index=True, autoincrement='ignore_fk')
    evid = Column(Integer, ForeignKey(Event.evid), primary_key=True, autoincrement='ignore_fk')

    course = relationship('Course', back_populates="events_for_course")
    event = relationship('Event', back_populates="events_for_course")


class EventParticipant(Base):
    __tablename__ = 'event_participants'
    uid = Column(Integer, ForeignKey(User.uid), primary_key=True, index=True, autoincrement='ignore_fk')
    evid = Column(Integer, ForeignKey(Event.evid), primary_key=True, autoincrement='ignore_fk')

    user = relationship('User', back_populates="event_participants")
