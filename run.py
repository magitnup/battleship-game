#Plan:
# 2 boards: one engine board and one player board
# engine board randomly selects places for ships
# player board allows for players choice to place ships
# validation for locking in the "goods" on the ships
# no repeat guesses, no out of bounds guesses
# smart guesses on the  side after a ship is found
# boards are 10x10 -> input 33 = row 3 column 3 starting with 0 - 9 for each
# decided on hit, miss, comp (completed) for clearer understanding

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
