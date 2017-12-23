from z3 import *

# Solving Puzzle
# Minesweeper is a game where we are given a matrix with some mines there.
# All cells are either contain the mine or a number which hint the number of mines
# in its surrounding.

# This can be used to track the location of bomb based on the hint we are given.
# It might not be used as a single solution and a one time pass, we need to incrementally
# update the known location.

known=[
"01?10001?",
"01?100011",
"011100000",
"000000000",
"111110011",
"????1001?",
"????3101?",
"?????211?",
"?????????"]

from z3 import *
import sys

WIDTH=len(known[0])
HEIGHT=len(known)

print "WIDTH=", WIDTH, "HEIGHT=", HEIGHT

def chk_bomb(row, col):

    s=Solver()

    cells=[[Int('cell_r=%d_c=%d' % (r,c)) for c in range(WIDTH+2)] for r in range(HEIGHT+2)]

    # make border
    for c in range(WIDTH+2):
        s.add(cells[0][c]==0)
        s.add(cells[HEIGHT+1][c]==0)
    for r in range(HEIGHT+2):
        s.add(cells[r][0]==0)
        s.add(cells[r][WIDTH+1]==0)

    for r in range(1,HEIGHT+1):
        for c in range(1,WIDTH+1):

            t=known[r-1][c-1]
            if t in "012345678":
                s.add(cells[r][c]==0)
                # we need empty border so the following expression would be able to work for all possible cases:
                s.add(cells[r-1][c-1] + cells[r-1][c] + cells[r-1][c+1] + cells[r][c-1] + cells[r][c+1] + cells[r+1][c-1] + cells[r+1][c] + cells[r+1][c+1]==int(t))

    # place bomb:
    s.add(cells[row][col]==1)

    result=str(s.check())
    if result=="unsat":
        print "row=%d col=%d, unsat!" % (row, col)

# enumerate all hidden cells:
for r in range(1,HEIGHT+1):
    for c in range(1,WIDTH+1):
        if known[r-1][c-1]=="?":
chk_bomb(r, c)

# Discussion
# https://news.ycombinator.com/item?id=13797375