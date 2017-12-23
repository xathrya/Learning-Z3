# Using `solve` function and Solver object to solve equations
#
# Use: 
#    python solve_solver.py 
# 

from z3 import *

x = Int('x')
y = Int('y')

# The goal is to find whether formulas is satisfiable
# Set of formulas is satisfiable if there is an interpretation that 
# makes all asserted formulas true.

# When checking for satisfiability, Z3 will returns `sat` for satisfiable
# or `unsat` for unsatisfiable. Z3 may also return `unknown` when it can't
# determine whether a formula is satisfiable or not.

#### solve()
# A function used to solve a system of equation
# it has some forms

# all equations are feeded as arguments
#   Declare: solve(formula)
solve(x > 2, y < 10, x + 2*y == 7)

# all equations are inside a list and then feeded to solve()
z = [x > 2, y < 10, x + 2*y == 7]
solve(z)

#### Solver
# An object used to solve a system of equation
# Equation is append to system
# satisfiability is check with .check()
s = Solver()
s.add(x > 2)                    # add single expression
s.add(y < 10, x + 2*y == 7)     # add multiple expression
z = [x > 0, y > 0]
s.add(z)                        # add list of expression

s.check()   # check for satisfiability, return: sat / unsat