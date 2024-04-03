#Plan:
# 2 boards: one engine board and one player board
# engine board randomly selects places for ships
# player board allows for players choice to place ships
# validation for locking in the "goods" on the ships
# no repeat guesses, no out of bounds guesses
# smart guesses on the  side after a ship is found
# boards are 10x10 -> input 33 = row 3 column 3 starting with 0 - 9 for each
# decided on hit, miss, comp (completed) for clearer understanding
# ships ... boats... ye...
# taken = so boats don't share the same fields on the board
#will add 1 or 2 to the different variables as to differentiate between board 1 and board 2

from random import randrange
import random

def get_shot(guesses):
    """
    checks for validity of the given variables and returns if necessary
    """
    ok = "n"
    while ok == "n":
        try:
            shot = input("please enter your guess")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("incorrect number, please try again")
            elif shot in guesses:
                print("incorrect number, used before")                
            else:
                ok = "y"
                break
        except:
            print("incorrect entry - please enter again")
             
    return shot

def show_board(hit,miss,comp):
    print("            battleships    ")
    print("     0  1  2  3  4  5  6  7  8  9")
 
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " x "
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " O "  
            row = row + ch
            place = place + 1
             
        print(x," ",row)
        

def check_shot(shot,ships,hit,miss,comp):
    """
     Checks if the shot is in the ships and returns the ships, hit, miss, comp, missed
     starts by checking if missed, because the chance of missing is the highest, followed by hit and completed
    """
    missed = 0
    for i in range(len(ships)):      
        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                comp.append(shot)
                missed = 2                             
    if missed == 0:
        miss.append(shot)
                 
    return ships,hit,miss,comp,missed

def check_ok(boat,taken):
    """
    checks if the ships have a valid length and starting point
    also decides the rotation of the ship
    """
    boat.sort()
    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [-1]
            break           
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(boat)-1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break
        if i != 0:
            if boat[i] != boat[i-1]+1 and boat[i] != boat[i-1]+10:
                boat = [-1]
                break
 
    return boat

def check_boat(b,start,dirn,taken):
    """
    checks if the boat is in the board and returns to boat
    """
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
    boat = check_ok(boat,taken)           
    return boat 

def create_boats(taken,boats):
    """
    creates a list of boats
    starting with position (anywhere from 00 to 99)
    to length and direction 0-4 for a 5 field ship and 0-1 for a 2 field ship
    planning for 6 boats per fleet/player/engine
    2 big ones 4 & 5 and 4 smaller ones with 3 & 2 twice each
    """
    ships = []
    #battleships = [5,4,3,3,2,2]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1,4)
            #print(b,boat_start,boat_direction)
            boat = check_boat(b,boat_start,boat_direction,taken)
        ships.append(boat)
        taken = taken + boat
        #print(ships)
        
    return ships,taken

#before game
hit1 = []
miss1 = []
comp1 = []
guesses1 = []  
missed1 = 0

taken1 = []
taken2 = []
hit2 = []
miss2 = []
comp2 = []
guesses2 = []  
missed2 = 0


battleships = [5,4,3,3,2,2]
# game amount of ships
#computer creates a board for player 1
ships1,taken1 = create_boats(taken1,battleships)
#user creates the board for player 2 - show board
ships2,taken2 = create_ships(taken2,battleships)
show_board_c(taken2)

# aware that there's currently some none defined variables.
# these are based on a guess of what I'll need for the future
# ready to add or remove if necessary