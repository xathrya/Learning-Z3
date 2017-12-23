# Z3 constraint solving in scope
# 
# Use: 
#    python scope.py 
# 
 
from z3 import *

x, y = Ints('x y')

s = Solver()

# Z3 maintains a stack of user provided formulas and declarations
# In some applications, we want to explore several similar problems
# that shares several definitions and assertions.

# Command push() create a new scope by saving the current stack size.
# Command pop() removes any assertion or declaration performed between it
# and the matching push.

# At first, it was empty
print(s)

# Base scope
s.add( x > 10, y == x + 2 )
print(s)
print("Solving constraints in the solver s ...")
print(s.check())

# Push the previous scope so we enter new scope (new frame)
print("Create a new scope")
s.push()
s.add(y < 11)
print(s)
print("Solving updated set of constraints ...")
print(s.check())

# Restoring the state to previous
print("Restoring state ...")
s.pop()
print(s)
print("Solving restored set of constraints ...")
print(s.check())