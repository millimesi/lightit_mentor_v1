#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_url = 'mysql+mysqlconnector://root:Million1234!@localhost/sqlalchemy_ex'

engine = create_engine(DB_url)
Session = sessionmaker(bind=engine)
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fname = Column(String(50))

# create all tables
Base.metadata.create_all(engine)
session = Session()

# create new user
# new_user = User(name='Million', fname='Meseret')
# session.add(new_user)
# session.commit()

# update user
user2 = session.query(User).filter_by(id=2).first()
if user2:
    user2.name = 'leti'
    session.commit()
# delete user
user_mi = session.query(User).filter_by(name='Million').first()
if user2:
    session.delete(user_mi)
    session.commit()
# read user
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.fname)

session.close
