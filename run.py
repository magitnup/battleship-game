#Plan:
# 2 boards: one computer board and one player board
# computer board randomly selects places for ships
# player board allows for players choice to place ships
# validation for locking in the "hits" on the ships
# no repeat guesses, no out of bounds guesses
# smart guesses on the computers side after hitting a ship
# boards are 10x10 -> input 33 = row 3 column 3 starting with 0 - 9 for each
def show_board(good,blunder,great):
    print("            battleships    ")
    print("     0  1  2  3  4  5  6  7  8  9")
 
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in blunder:
                ch = " x "
            elif place in good:
                ch = " o "
            elif place in great:
                ch = " s "  
            row = row + ch
            place = place + 1
             
        print(x," ",row)
        
blunder = [0,1,2,3,4,5,6,7,8,9]

good = [10,11,12,13,14,15,16,17,18,19]

great = [20,21,22,23,24,25,26,27,28,29]


show_board(blunder, good, great)