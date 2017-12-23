'''Light Up solver in Z3.

Light Up is a perfect-information logic puzzle with simple rules.
There is a free online implementation at, for instance,
https://www.puzzle-light-up.com/.

The rules are as follows: Light Up is played on a rectangular
grid. The grid has both black cells and white cells in it. The
objective is to place light bulbs on the grid so that every white
square is lit. A cell is illuminated by a light bulb if they're in the
same row or column, and if there are no black cells between
them. Also, no light bulb may illuminate another light bulb.  Some of
the black cells have numbers in them. A number in a black cell
indicates how many light bulbs share an edge with that cell.

This module encodes that puzzle definition as a finite-domain
constraint satisfaction problem and solves it with Z3
(https://github.com/Z3Prover/z3).  In my limited testing, Z3 finds
solutions to puzzles up to 40x30 in a matter of seconds.

For this to work, run it in a virtualenv that has the Z3 python
bindings installed.
'''

import sys
import z3

# A puzzle definition is row-major top-down list of lists entries.
# An entry gives the state of a cell: clear, blocked, or number, where
# the number gives the number of bulbs next to that cell.

# The readable representation of the puzzle is a list of rows, where
# each row is a string.  The row has exactly one character per cell:
# '.' for blank, 'X' for blocked, and a digit for that many bulbs
# being there.

puzzle_5 = [
  "....0..",
  "...1X..",
  "X1.....",
  ".1...2.",
  ".....X2",
  "..10...",
  "..1...."
]

puzzle_14 = [
  ".X.....3.2....",
  "...XX.X.X..2.2",
  ".0.X..........",
  ".....1...X.XX.",
  "2..1.X..0...X.",
  ".X..X..X.XX...",
  "X....X......2.",
  ".2......X....X",
  "...02.X..4..X.",
  ".X...X..X.X..X",
  ".XX.1...1.....",
  "..........1.1.",
  "X.2..X.X.XX...",
  "....X.2.....0.",
]

# Special at https://www.puzzle-light-up.com/ for October 2, 2017.
# 20 minutes of copy-typing (including the solution); 3 seconds to solve.
puzzle_special = [
  "....11...X.X.3...X.X.X....1...",
  ".....1....XX......X.X....2....",
  "XX......1X..X.X..XXX....X.X01X",
  "X0.X...XXX..X0..X1...2.0....2.",
  "........1.0......XX.....2.X...",
  "2.X..XX.....2.X...........X.X.",
  "XXXX.X.XX...1X............X.2.",
  ".X......1.X.......X.1...0.....",
  "X.X..12..2.....X1.X..1.....X..",
  "X..X......XXX.0X..0.XX.1.2...X",
  "..X.XX..2.1X..1.X.X.2.X...2...",
  "....X..........X.0...X....X..2",
  "0.11.XX..X0X0............2.XX.",
  "X..XX2.X.0.....XX...1X....X1.1",
  "...X...XX0...00XX....10.1.....",
  "......XX............X.....X...",
  "X....1X....X..XXX.1......X....",
  "......1..2XX........1...1X2...",
  "3.....XXX.XXX.3...0.X....3.X0X",
  "..X..XX....1.X..2.XXXXXX..XXXX",
  ".1.1...2..X.XXX...XX.....1...X",
  "X.2..X1...0.X......3.1....XX2.",
  "....XX..XXX.X..1.......XXX....",
  "....X..4...X....X.X.XX...X2.XX",
  "XX..0.X....X2..X.X.XX...XX..XX",
  "....X...X.........X.XX..XX3...",
  "...X.1XX....X..XXX....X.....0.",
  "......X..00X1.X...2.X1..3.X...",
  "..X0...4..XXXXX..1X..X....XX..",
  "..0..X..X..XX.....XX....XX1...",
  ".2..3..X..XX..1..XX.X1.3..XX1.",
  ".....X...0.2.XX0...XXX..XX..X.",
  ".....XXX.2........0X0.XX.XX...",
  "............1......X..1..1X.2X",
  "...XXX...X..XXX......3......X.",
  "..2.X1....X.XX.X....X.2...XX.X",
  "X0.1........0X2....2..X1...X.X",
  ".....0.1.1X..X.X.2..X0...XX.3X",
  "......2.X.X.....X...0.....2...",
  ".X2..X...XX.X.XX.XX..XXX...XX.",
]

block = 'block'

def parse_char(c):
  if c == '.':
    return None
  if c == 'X':
    return block
  return int(c)

def parse(puzzle):
  return [[parse_char(c) for c in row] for row in puzzle]

def lightup(puzzle):
  '''Encode a parsed puzzle definition as a collection of Z3 constraints.

  Choice of encoding: For every blank cell, I define an integer that
  is 1 if the cell contains a blub and 0 if not.  (Not a boolean,
  because I wasn't sure that Z3 would pun booleans to Bernoulli
  variables when I wanted to sum them.)

  Return a 2-tuple of the Z3 solver object representing the puzzle,
  and the row-major list of lists of those integers (or 0 for black
  cells).
  '''

  # Convention: i indexes rows, j indexes columns
  s = z3.Solver()
  def has_light(i, j, obstacle):
    '''The variable for whether a given position has a light, depending on
what obstacle puzzle definition has there.'''
    if obstacle == None:
      light = z3.Int('light %d %d' % (i, j))
      s.add(light >= 0)
      s.add(light <= 1)
      return light
    return 0
  # The light variables
  lights = [[has_light(i, j, item) for (j, item) in enumerate(row)]
            for (i, row) in enumerate(puzzle)]
  # Querying for a bulb, possibly outside the grid (which does not
  # have bulbs).
  def get_light(i, j):
    if 0 <= i and i < len(lights) and 0 <= j and j < len(lights[0]):
      return lights[i][j]
    return 0

  # Yield all the cells that can be seen from the given coordinates
  # (as a function of what obstacles are where).
  def walk_visible_spaces(i0, j0):
    if lights[i0][j0] is 0:
      return
    for i1 in range(i0+1, len(puzzle)):
      # Walk down
      if lights[i1][j0] is 0:
        # There is an obstacle here
        break
      yield (i1, j0)
    for i1 in range(i0-1, -1, -1):
      # Walk up
      if lights[i1][j0] is 0:
        # There is an obstacle here
        break
      yield (i1, j0)
    for j1 in range(j0+1, len(puzzle[0])):
      # Walk right
      if lights[i0][j1] is 0:
        # There is an obstacle here
        break
      yield (i0, j1)
    for j1 in range(j0-1, -1, -1):
      # Walk left
      if lights[i0][j1] is 0:
        # There is an obstacle here
        break
      yield (i0, j1)

  # No two lights shine on each other
  for i0 in range(len(puzzle)):
    for j0 in range(len(puzzle[0])):
      for (i1, j1) in walk_visible_spaces(i0, j0):
        if i1 > i0 or j1 > j0:
          s.add(lights[i0][j0] + lights[i1][j1] < 2)
        else:
          # Avoid adding the same constraint twice
          pass

  # Each digit gives the number of adjacent lights
  for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
      if isinstance(puzzle[i][j], int):
        near_lights = get_light(i-1, j) + get_light(i, j-1) + get_light(i, j+1) + get_light(i+1, j)
        constraint = near_lights == puzzle[i][j]
        s.add(constraint)

  # Every blank square is lit
  for i0 in range(len(puzzle)):
    for j0 in range(len(puzzle[0])):
      if lights[i0][j0] is 0:
        continue
      candidates = [lights[i0][j0]]
      for (i1, j1) in walk_visible_spaces(i0, j0):
        candidates.append(lights[i1][j1])
      s.add(sum(candidates) >= 1)

  return (s, lights)

def render(model, puzzle, lights):
  '''Render the given solution in ASCII art.  Show an 'o' for every light bulb.'''
  def render_one(i, j):
    if puzzle[i][j] is None:
      # Blank cell
      if model[lights[i][j]] == 1:
        # Light bulb
        return 'o'
      else:
        return '.'
    if puzzle[i][j] == block:
      return 'X'
    return str(puzzle[i][j])
  for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
      sys.stdout.write(render_one(i, j))
    print ""

def solve(puzzle):
  '''Fully solve the given Light Up puzzle, and print the solution as
  ASCII art if it exists.'''
  puzzle = parse(puzzle)
  (s, lights) = lightup(puzzle)
  # print s.sexpr()
  # print lights
  res = s.check()
  if res == z3.sat:
    print "Solution"
    m = s.model()
    # print m
    render(m, puzzle, lights)
  else:
    print "Unsolvable because"
    print s.unsat_core()

if __name__ == '__main__':
  solve(puzzle_special)
