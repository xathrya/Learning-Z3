# Some basic integer math
#
# Use: 
#    python int-math.py 
# 
from z3 import *

### Check multiplication laws
def check_multiplication_laws_1():
    a = Int('a')
    b = Int('b')
    print("Checking if (a+b)(a-b) == a*a-b*b")
    prove((a+b)*(a-b) == a*a - b*b)

### Check inequalities
def check_inequalities():
    a = Int('a')
    b = Int('b')
    solver = Solver()
    print("Checking if a+b >= a")
    solver.add(a+b >= a)
    print(solver.check())
    print(solver.model())

    print("Checking if a+b >= a if a,b >= 0")
    solver.add(a >= 0, b >= 0)
    print(solver.check())
    print(solver.model())

check_multiplication_laws_1()
check_inequalities()