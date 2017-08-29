import random
import sys
import os

age = 30

if age > 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

if age >=21:
    print('You are old enough to drive tractor trailer')
elif age >= 16:
    print('You are old enough to drive')
else:
    print("You are not old enough to drive")

if ((age >=1) and (age<= 18)):
    print("You get a birthday")
elif (age == 21) or (age == 65):
    print("You get a birthday")
elif not(age == 30):
    print("You dont get a birthday")
else:
    print("You get a birthday party yeah")
