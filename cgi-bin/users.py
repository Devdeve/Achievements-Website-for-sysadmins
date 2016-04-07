#!/usr/bin/python2

from database import User, UserAchievement, setup
from json import dumps

print "Content-Type: application/json"
print 

session = setup()

all_users = {}
for u in session.query(User).all():
    all_users[u.displayname] = u.user

print dumps(all_users)