import sys
import time
from z3 import *

def solve_magic_square(size):
    """Try to a solution for a size-magic square"""
    def column(matrix, i):
        """Get the column i of matrix"""
        return [matrix[j][i] for j in range(size)]

    def get_diagonals(matrix):
        """Get the diagonals of matrix"""
        return ([matrix[i][i] for i in range(size)], [matrix[i][size - i - 1] for i in range(size)])

    def get_constrained_int(x, y, s):
        """Get an Int and add the constraints associated directly in the solver"""
        # Int() is really really slower!
        x = BitVec('x%dy%d' % (x, y), 32)
        s.add(x > 0, x <= size**2)
        return x

    s = Solver()
    magic = (size * (size**2 + 1)) / 2
    matrix = [[get_constrained_int(y, x, s) for y in range(size)] for x in range(size)]

    # Each value must be different
    s.add(Distinct([matrix[i][j] for j in range(size) for i in range(size)]))

    for i in range(size):
        # Sum of each line, column must be equal to magic
        s.add(Sum(matrix[i]) == magic, Sum(column(matrix, i)) == magic)

    # Sum of each diagonal must be equal to magic
    d1, d2 = get_diagonals(matrix)
    s.add(Sum(d1) == magic, Sum(d2) == magic)

    if s.check() == unsat:
        raise Exception('The problem is not sat')

    m = s.model()
    return [[m[val].as_long() for val in line] for line in matrix], magic

def display_magic_square(s, magic):
    """Display the magic square with the solution"""
    print('Magic value: %d' % magic)
    for i in range(len(s)):
        print('%.3d|' * len(s) % tuple(s[i]))

def main(argc, argv):
    if argc < 2:
        print('Usage: ./magic_square_z3 <n>')
        return -1

    n = int(argv[1], 10)
    print('Trying to find a solution for a %d-magic square..' % n)
    t1 = time.time()
    s, magic = solve_magic_square(n)
    t2 = time.time()

    print('Found a solution in %ds:' % (t2 - t1))
    display_magic_square(s, magic)
    return 1

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))