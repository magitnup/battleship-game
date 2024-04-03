from random import randrange
import random

# Plan:
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
# will add 1 or 2 to the different variables as to
# differentiate between board 1 and board 2
# realized that I needed tactics for the engine to
# not only randomly guess every turn
# credits to my brother for hinting me in the right direction of how
# * let engine continue guessing near successful hits

def check_ok(boat, taken):
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


def get_ship(long, taken):
    """
    so the player can choose where to put his fleet
    also prevents the stacking of ships on the same field
    """
    ok = True
    while ok:
        ship = []
        # ask the user to enter numbers
        print("Enter your ship of length ", long)
        for i in range(long):
            boat_num = input("Please enter a number\n")
            ship.append(int(boat_num))
        ship = check_ok(ship, taken)
        if ship[0] != -1:
            taken = taken + ship
            break
        else:
            print("Error - Please try again")

    return ship, taken


def create_ships(taken, boats):
    # create a list of ships
    ships = []
    for boat in boats:
        ship, taken = get_ship(boat, taken)
        ships.append(ship)

    return ships, taken


def check_boat(b, start, checkup, taken):
    """
    checks if the boat is in the board and returns to boat
    """
    boat = []
    if checkup == 1:
        for i in range(b):
            boat.append(start - i*10)
    elif checkup == 2:
        for i in range(b):
            boat.append(start + i)
    elif checkup == 3:
        for i in range(b):
            boat.append(start + i*10)
    elif checkup == 4:
        for i in range(b):
            boat.append(start - i)
    boat = check_ok(boat, taken)
    return boat


def create_boats(taken, boats):
    """
    creates a list of boats
    starting with position (anywhere from 00 to 99)
    to length and direction 0-4 for a 5 field ship and 0-1 for a 2 field ship
    planning for 6 boats per fleet/player/engine
    2 big ones 4 & 5 and 4 smaller ones with 3 & 2 twice each
    """
    ships = []
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 4)
            boat = check_boat(b, boat_start, boat_direction, taken)
        ships.append(boat)
        taken = taken + boat

    return ships, taken

def show_board_engine(taken):
    print("     BATTLESHIPS YOUR BOARD    ")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in taken:
                ch = " o "
            row = row + ch
            place = place + 1

        print(x, " ", row)


def get_shot_engine(guesses, tactics):
    # forgot to bring this over from the testing grounds
    ok = "n"
    while ok == "n":
        try:
            if len(tactics) > 0:
                shot = tactics[0]
            else:
                shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
        except:
            print("Invalid entry - Please try again")

    return shot, guesses


def show_board(hit, miss, comp):
    """
    shows the board
    """
    print("     BATTLESHIPS ENEMY BOARD    ")
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
                ch = " s "
            row = row + ch
            place = place + 1

        print(x, " ", row)


def check_shot(shot, ships, hit, miss, comp):
    """
     Checks if the shot is in the ships and
     returns the ships, hit, miss, comp, missed
     starts by checking if missed, because the chance of
     missing is the highest, followed by hit and completed
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

    return ships, hit, miss, comp, missed


def calc_tactics(shot, tactics, guesses, hit):
    """
    calculates the tactics for the given shot of the engine
    """
    # credits to my brother for explaining to me how
    # it's done, he's probably my best teacher.
    # would have to revisit the course to see if I can
    # figure this out in a better way (but time troubles).
    temp = []
    if len(tactics) < 1:
        temp = [shot-1, shot+1, shot-10, shot+10]
    else:
        if shot-1 in hit:
            temp = [shot+1]
            for num in [2, 3, 4, 5, 6, 7, 8]:
                if shot-num not in hit:
                    temp.append(shot-num)
                    break
        elif shot+1 in hit:
            temp = [shot-1]
            for num in [2, 3, 4, 5, 6, 7, 8]:
                if shot+num not in hit:
                    temp.append(shot+num)
                    break
        if shot-10 in hit:
            temp = [shot+10]
            # full credit to my brother for the "20, 30, 40, ..." part
            for num in [20, 30, 40, 50, 60, 70, 80]:
                if shot-num not in hit:
                    temp.append(shot-num)
                    break
        elif shot+10 in hit:
            temp = [shot-10]
            for num in [20, 30, 40, 50, 60, 70, 80]:
                if shot+num not in hit:
                    temp.append(shot+num)
                    break

    impossible = []
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            impossible.append(temp[i])
    random.shuffle(impossible)

    return impossible


def get_shot(guesses):
    """
    checks for validity of the given variables and returns if necessary
    """
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess\n")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("Invalid number, please try again")
            elif shot in guesses:
                print("Invalid number, used before")
            else:
                ok = "y"
                break
        except:
            print("Invalid entry - please try again")

    return shot


def check_if_empty_2(list_of_lists):
    return all([not elem for elem in list_of_lists])


# before game
hit1 = []
miss1 = []
comp1 = []
guesses1 = []
missed1 = 0
tactics1 = []
taken1 = []
# separate the two boards a bit
hit2 = []
miss2 = []
comp2 = []
guesses2 = []
missed2 = 0
tactics2 = []
taken2 = []

battleships = [5, 4, 3, 3, 2, 2]
# amount of ships on the field
# computer creates a board for player 1
ships1, taken1 = create_boats(taken1, battleships)
# user creates the board for player 2 - show board
ships2, taken2 = create_ships(taken2, battleships)
show_board_engine(taken2)

# loop
for i in range(80):
    """
    Players shots on "ENEMY BOARD"
    """
    guesses1 = hit1 + miss1 + comp1
    shot1 = get_shot(guesses1)
    ships1, hit1, miss1, comp1,
    missed1 = check_shot(shot1, ships1, hit1, miss1, comp1)
    show_board(hit1, miss1, comp1)
# repeat until ships empty
    if check_if_empty_2(ships1):
        print("End of Game - You Win!", i)
        break

# engines shots "YOUR BOARD"
    shot2, guesses2 = get_shot_engine(guesses2, tactics2)
    ships2, hit2, miss2, comp2,
    missed2 = check_shot(shot2, ships2, hit2, miss2, comp2)
    show_board(hit2, miss2, comp2)

    if missed2 == 1:
        tactics2 = calc_tactics(shot2, tactics2, guesses2, hit2)
    elif missed2 == 2:
        tactics2 = []
    elif len(tactics2) > 0:
        tactics2.pop(0)

    if check_if_empty_2(ships2):
        print("End of game - You Lose", i)
        break
