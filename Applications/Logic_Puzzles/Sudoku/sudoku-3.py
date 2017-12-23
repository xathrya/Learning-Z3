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

s = Solver()

# Using python list comprehension, construct array of arrays of BitVec
cells = [[Int('cell%d%d' %( r, c)) for c in range(9)] for r in range(9)]

# http://www.norvig.com/sudoku.html
# http://www.mirror.co.uk/news/weird-news/worlds-hardest-sudoku-can-you-242294
puzzle="..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97.."

# Process text line:
current_column = 0
current_row = 0
for i in puzzle:
    if i != '.':
        s.add(cells[current_row][current_column] == int(i))
    current_column = current_column + 1
    if current_column == 9:
        current_column = 0
        current_row = current_row + 1

# Important, Z3 will report correct solutions with too bigh and/or negative numbers in cells
cells_c = [ And(1 <= cells[r][c], cells[r][c] <= 9) for c in range(9) for r in range(9) ]

# For all 9 rows
rows_c  = [ Distinct( cells[r] ) for r in range(9) ]

# For all 9 columns
cols_c  = [ Distinct( [ cells[r][c] for r in range(9) ] ) for c in range(9) ]

# Enumerate all 9 squares
square_c = [ Distinct( [ cells[3*r0 + r][3*c0 + c] for r in range(3) for c in range(3) ] ) for r0 in range(3) for c0 in range(3) ]

s.add(cells_c + rows_c + cols_c + square_c)

result = []
i = 1
while s.check() == sat and i < 5:
    m = s.model()
    result.append(m)

    print("Result %d" % i)
    i = i + 1
    for r in range(9):
        for c in range(9):
            sys.stdout.write (str(m[cells[r][c]])+" ")
            if (c == 2) or (c == 5):
                sys.stdout.write("| ")
        print("")
        if (r == 2) or (r == 5):
            print("----------------------")
    
    # Create new constraint the blocks the current model
    block = []
    for el in m:
        # el is a declaration
        if el.arity() > 0:
            raise Z3Exception("uninterpreted function are not supported")
        
        # Create a constant from declaration
        obj = el() 

        if is_array(obj) or obj.sort().kind() == Z3_UNINTERPRETED_SORT:
            raise Z3Exception("arrays and uninterpreted sorts are not supported")
        
        block.append(obj != m[el])
    
    s.add(Or(block))