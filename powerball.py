# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:57:15 2017

Powerball Game

V 0.5 - Work in progress


-***REMOVED*** Kay



@author: orpha
"""
from numpy import random

# # # # # # # #
def powerball_input():
    print("Welcome to Powerball!") 
    # The game data.
    white_balls = [0,0,0,0,0]
    red_ball = 0
    # The name data.
    are_you_sure = "Nope."
    while are_you_sure[0].lower() != "y":
        name = str(input("Please enter your name..."))
        are_you_sure = str(input("Are you sure your name is {0}... y/n?".format(name)))
    print("Thanks, {0}.".format(name))      
    
    for i in range(0,5):
        while True:
            try:
                number = int(input('Please pick your #{0} white ball in the range of 1-69: ...'.format(str(i + 1))))
                # Good cases may occur here
            except ValueError as e:
                print("... as alphanumeric characters 0-9...")
                continue
        #        number = int(input('input a number...'))
            if number < 1:
                print("... please enter your number within the range of 1-69")
                continue
            if number > 69:
                print("... please enter your number within the range of 1-69")
                continue
            if number in white_balls:
                print("each pick must be unique...")
                continue
            else:
                white_balls[i] = number
                break
    while True:
        try:
            red_ball = int(input('Please pick your red ball number in the range of 1-26: ...'))
        except ValueError as e:
            print("... as alphanumeric characters 0-9...")
            continue
        if number < 1:
            print("... please enter your number within the range of 1-26")
            continue
        if number > 26:
            print("... please enter your number within the range of 1-26")
            continue
        break
    return(name, white_balls, red_ball)

entries = []
while len(entries) < 2: # How many entries? Set as parameter.
    entries.append(powerball_input())

# entries = [('Emzilla', [1, 2, 3, 4, 5], 6), ('KayKilla', [1, 2, 3, 4, 5], 6)]
# entries = [('Mary', [7, 21, 33, 66, 13], 6), ('Sue', [13, 33, 66, 2, 1], 6)]
# # # # # Scoring section # # # # # 
 
#entries_dict = {row[0]: row[1:] for row in entries}
#def powerball_scoring()
white_ball_picks = dict()
for entry in entries:
        for n in entry[1]:
            if n in white_ball_picks:
                white_ball_picks[n] += 1
            else:
                white_ball_picks.setdefault(n, 1)
del entry, n

top_5_picks = [0,0,0,0,0] # Object to store most popular white ball picks.

for n in range(0,4):
    white_ball_max = [(0,0)]
    for i in white_ball_picks.items():
#        print(i)    #i == k, v
        if white_ball_max[0][1] < i[1]:
            white_ball_max[0] = i
        if white_ball_max[0][1] == i[1]:
            white_ball_max.append(i)
        else:
            continue
    if len(white_ball_max) == 1: # In the case of no tie.
          top_5_picks[n] = white_ball_max[0][0]
          del white_ball_picks[white_ball_max[0][0]]
    else: #In case of a tie.
        rand = np.random.randint(1,len(white_ball_max))
        top_5_picks[n] = white_ball_max[rand][0]
        del white_ball_picks[white_ball_max[rand][0]]
    
top_5_picks

    