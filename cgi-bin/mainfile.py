#!/usr/bin/python2
from go import mainJSON
import cgitb
import cgi
from database import User, UserAchievement, setup
from json import dumps

cgitb.enable()
form = cgi.FieldStorage()
name = form.getvalue('name')

print "Content-Type: application/json"
print

data = {}

if name:
    session = setup()

    user = session.query(User).filter_by(user=name).first()

    data = mainJSON(user.points)
    data["displayname"] = user.displayname

print dumps(data)

