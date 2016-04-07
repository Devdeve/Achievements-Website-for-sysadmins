import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user = Column(String, primary_key=True)
    displayname = Column(String)
    password = Column(String)
    points = Column(Integer, default=0)
    def __repr__(self):
        return "<User(displayname='%s', password='%s')>" % (self.displayname, self.password)
    
class UserAchievement(Base):
    __tablename__ = "UserAchievements"
    user = Column(String, primary_key=True)
    achievement = Column(String, primary_key=True)
    def __repr__(self):
        return "<UserAchievement(user='%s', achievement='%s')>" % (self.user, self.achievement) 
        
class Achievement(Base):
    __tablename__ = "Achievements"
    internal = Column(String, primary_key=True)
    external = Column(String)
    points = Column(Integer)
    def __repr__(self):
        return "<(internal='%s', external='%s')>" % (self.internal, self.external) 
        
def setup(): 
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    return session
