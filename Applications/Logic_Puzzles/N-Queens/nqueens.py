from z3 import *
from builtins import input
from pprint import pprint
import sys

def display_board(s):
    board = [[0] * len(s) for i in range(len(s))]
    for x, y in s:
        board[x][y] = 1
    pprint(board)

def abs_z3(a):
    return If(a >= 0, a, -a)

def solve_nqueens(n):
    # Queen at which column?
    columns = [Int('c%d' %i) for i in range(n)]
    # Set each column at a specific value, 0..N, it avoids a lot of useless constrains
    lines = range(n)
    s = Solver()

    for i in range(n):
        s.add(columns[i] >= 0, columns[i] < n)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            s.add(columns[i] != columns[j])
            s.add(lines[i] != lines[j])
            s.add(abs_z3(columns[i] - columns[j]) != abs(lines[i] - lines[j]))
    
    if s.check() == unsat:
        raise Exception('Unsat bitch')
    
    m = s.model()
    return [(m[x].as_long(), y) for x, y in zip(columns, lines)]

def main(argc, argv):
    nqueens = 0
    if argc < 2:
        nqueens = input('N= ')
    else:
        nqueens = int(sys.argv[1])

    print("Using %d queens" % nqueens)
    sol = solve_nqueens(nqueens)
    display_board(sol)

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)