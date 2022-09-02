# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:57:15 2017

Powerball Game
June 20-22

Developed in Python 3.6.0 |Anaconda 4.3.0 (64-bit)

Development time : 4-5 hours

@author: github.com/Emzilla-01
"""
from numpy import random

# # # # # #

parameter_numberof_entries = 2 # This parameter determines how many contestants are playing Powerball.


# # # # # # # #
# Definition of powerball_input() function.
# powerball_input() takes 'validated' input from the user and outputs a tuple:
# ("name", [5 unique white ball picks], int(1 red ball pick))

def powerball_input():
    print("Welcome to Powerball!") 
    # The game data.
    white_balls = [0,0,0,0,0]
    red_ball = 0
    # The name data.
    are_you_sure_first = "Nope."
    are_you_sure_last = "Negative."
    
    while are_you_sure_first[0].lower() != "y":
        first_name = str(input("Please enter your first name..."))
        are_you_sure_first = str(input("Are you sure your first name is {0}... y/n?".format(first_name)))
   
    while are_you_sure_last[0].lower() != "y":
        last_name = str(input("Please enter your last name..."))
        are_you_sure_last = str(input("Are you sure your last name is {0}... y/n?".format(last_name)))
    name = first_name + " " + last_name
    
    print("Thanks, {0}.".format(name))      
    
    for i in range(0,5):
        while True:
            try:
                if i == 0:
                    number = int(input('Please pick your #{0} white ball in the range of 1-69: ...'.format(str(i + 1))))
                if i>0:
                    number = int(input('Please pick your #{0} white ball in the range of 1-69, {1}: ...'.format(str(i + 1), "excluding {0}".format(str(white_balls[:i]).strip("[]") ) )  ))
                # Good cases may occur here
            except ValueError as e:
                print("... as alphanumeric characters 0-9...")
                continue
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
        else:
            break
    return(name, white_balls, red_ball)



# Definition of scoring() function.
# scoring() takes entries as input. Expects entries as the output of powerball_input().
def scoring(entries):
    white_ball_picks = dict()
    red_ball_picks = dict()
    for entry in entries:
            #White ball counts
            for n in entry[1]:
                if n in white_ball_picks:
                    white_ball_picks[n] += 1
                else:
                    white_ball_picks.setdefault(n, 1)
            del n
            #Red ball counts
            if entry[2] in red_ball_picks:
                red_ball_picks[entry[2]] += 1
            else:
                red_ball_picks.setdefault(entry[2], 1)
#    del entry, n            
    
    top_5_picks = [0,0,0,0,0] # Object to store most popular white ball picks.
    red_ball_max = [(0,0)]
    
    for n in range(0,5):
        white_ball_max = [(0,0)]
        for i in white_ball_picks.items():
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
            rand = random.randint(1,len(white_ball_max))
            top_5_picks[n] = white_ball_max[rand][0]
            del white_ball_picks[white_ball_max[rand][0]]
    del n
    
    for n in red_ball_picks.keys():
        if red_ball_picks.get(n) > red_ball_max[0][1]:
            red_ball_max = [(n, red_ball_picks.get(n))]
        if red_ball_picks.get(n) == red_ball_max[0][1]:            
            red_ball_max.append((n, red_ball_picks.get(n)))
            
    if len(red_ball_max) > 1:
        red_ball_max = red_ball_max[random.randint(0, len(red_ball_max))][0]
                                  
    return((top_5_picks), red_ball_max)

# # # # 


entries = []
while len(entries) < parameter_numberof_entries: #
    entries.append(powerball_input())

winning_numbers = scoring(entries)

for entry in entries:
    print("Contestant : {0}, White ball picks: {1}, Red ball pick: {2}".format(entry[0], str(entry[1]).strip("[]"), entry[2]))

print("Winning Numbers : {0}, Powerball : {1}".format(str(winning_numbers[0]).strip("[]"), winning_numbers[1])) 

print("Thank you for playing Powerball.")
 
