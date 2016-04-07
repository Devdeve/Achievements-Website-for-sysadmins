#!/usr/bin/python2

from database import Achievement, setup

session = setup()

f = open('achievements.txt')

for line in f:
    external = line.split('-')[0].strip()
    internal = external.lower().translate(None, ',.?! ')
    session.add(Achievement(internal=internal, external=external))
session.commit()