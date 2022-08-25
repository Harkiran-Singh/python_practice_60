"""Story Generator
This script  generate a random story every time the user runs the program

This tool doesn't require any input from the user

The script uses python 'random' module
"""

import random

when = ['Once upon a time', 'Last night', 'Day before', 'Last week', 'Long time ago']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
residence = ['India', 'Barcelona', 'Germany', 'Venice', 'England']
name = ['Ali', 'Miriam', 'Daniel', 'Houuk', 'Star-walker']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'wrote a book', 'solved a mystery']

print(random.choice(when) + ', ' + random.choice(name) + ' and ' + random.choice(who) + ' that lived in '
      + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))

#print(random.sample(when, k=2))
