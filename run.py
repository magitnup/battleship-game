#Plan:
# 2 boards: one computer board and one player board
# computer board randomly selects places for ships
# player board allows for players choice to place ships
# validation for locking in the "hits" on the ships
# no repeat guesses, no out of bounds guesses
# smart guesses on the computers side after hitting a ship
# boards are 10x10 -> input 33 = row 3 column 3 starting with 0 - 9 for each
print("     BATTLESHIPS:    ")
print("   0  1  2  3  4  5  6  7  8  9")
for x in range(10):
    print(x," _ "*10)
