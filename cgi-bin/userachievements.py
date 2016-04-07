#!/usr/bin/python2


from database import User, UserAchievement,Achievement, setup
from json import dumps

import cgitb
import cgi
cgitb.enable()
form = cgi.FieldStorage()
name = form.getvalue('name')

print "Content-Type: application/json"
print 

session = setup()

all_userachievements = {
    'unlocked' : {},
    'locked' : {},
}

for a in session.query(Achievement).all():
    all_userachievements['locked'][a.internal] = a.external
    
for u in session.query(UserAchievement).filter_by(user=name).all():
    all_userachievements['unlocked'][u.achievement] = all_userachievements['locked'][u.achievement]
    del all_userachievements['locked'][u.achievement]
 
print dumps(all_userachievements)