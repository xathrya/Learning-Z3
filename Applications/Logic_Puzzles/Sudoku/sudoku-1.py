import sys
from z3 import *
"""
coordinates:
------------------------------
00 01 02 | 03 04 05 | 06 07 08
10 11 12 | 13 14 15 | 16 17 18
20 21 22 | 23 24 25 | 26 27 28
------------------------------
30 31 32 | 33 34 35 | 36 37 38
40 41 42 | 43 44 45 | 46 47 48
50 51 52 | 53 54 55 | 56 57 58
------------------------------
60 61 62 | 63 64 65 | 66 67 68
70 71 72 | 73 74 75 | 76 77 78
80 81 82 | 83 84 85 | 86 87 88
------------------------------
"""

# The idea
# All possible numbers have shown up, nothing is used twice nor not exists
# in each row or column
# The "existence" is defined by a mask of bit 

s = Solver()

# Using python list comprehension, construct array of arrays of BitVec
cells = [[BitVec('cell%d%d' %( r, c), 16) for c in range(9)] for r in range(9)]

# http://www.norvig.com/sudoku.html
# http://www.mirror.co.uk/news/weird-news/worlds-hardest-sudoku-can-you-242294
puzzle="..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97.."

# Process text line:
current_column = 0
current_row = 0
for i in puzzle:
    if i != '.':
        s.add(cells[current_row][current_column] == BitVecVal(int(i), 16))
    current_column = current_column + 1
    if current_column == 9:
        current_column = 0
        current_row = current_row + 1

one = BitVecVal(1, 16)
mask = BitVecVal(0b1111111110, 16)

for r in range(9):
    s.add(((one<<cells[r][0]) +
        (one<<cells[r][1]) +
        (one<<cells[r][2]) +
        (one<<cells[r][3]) +
        (one<<cells[r][4]) +
        (one<<cells[r][5]) +
        (one<<cells[r][6]) +
        (one<<cells[r][7]) +
        (one<<cells[r][8]))==mask)
# for all 9 columns
for c in range(9):
    s.add(((one<<cells[0][c]) +
        (one<<cells[1][c]) +
        (one<<cells[2][c]) +
        (one<<cells[3][c]) +
        (one<<cells[4][c]) +
        (one<<cells[5][c]) +
        (one<<cells[6][c]) +
        (one<<cells[7][c]) +
        (one<<cells[8][c]))==mask)
# enumerate all 9 squares
for r in range(0, 9, 3):
    for c in range(0, 9, 3):
    # add constraints for each 3*3 square:
        s.add((one<<cells[r+0][c+0]) +
            (one<<cells[r+0][c+1]) +
            (one<<cells[r+0][c+2]) +
            (one<<cells[r+1][c+0]) +
            (one<<cells[r+1][c+1]) +
            (one<<cells[r+1][c+2]) +
            (one<<cells[r+2][c+0]) +
            (one<<cells[r+2][c+1]) +
            (one<<cells[r+2][c+2])==mask)
#print s.check()
s.check()
#print s.model()
m=s.model()
for r in range(9):
    for c in range(9):
        sys.stdout.write (str(m[cells[r][c]])+" ")
        if (c == 2) or (c == 5):
            sys.stdout.write("| ")
    print("")
    if (r == 2) or (r == 5):
        print("----------------------")