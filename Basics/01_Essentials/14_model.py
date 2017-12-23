#
# Goal: 
#    Traversing the model and alternative solution
# Use: 
#    python model.py 
# 

from z3 import *

x, y, z = Reals('x y z')

# Create a solver object
s = Solver()

# Add constraint (to current scope)
s.add(x > 1, y > 1, x + y > 3, z - x < 10)

# Check if there is a solution (all equation satisfied)
print(s.check())

# Get the model (value that instantiate the object which gives satisfying equation)
m = s.model()
print("Traversing model")
for d in m.decls():
    print("{} = {}".format(d.name(), m[d]))

# Get alternative model
# Add current result to the constraint, which shall be excluded
print("Alternative")
block = []
for el in m:
    obj = el()
    block.append(obj != m[el])
s.add(Or(block))
print(s.check())

m = s.model()
print("Traversing model")
for d in m.decls():
    print("{} = {}".format(d.name(), m[d]))

# We can also get instance of each the variable on model
# Accessing variable x on model such as m[x] gives the instance of that
# constrained variable. However, to obtain the concrete value, we need to 
# apply cast before using it.

# We can also test whether m[x] is obtained as a rational number
if is_rational_value(m[x]):
    # Cast as reals
    m[x].as_fraction()  # exact rational number

    # We can also get the real value as denominator and numerator separately
    m[x].denominator_as_long()
    m[x].numerator_as_long()
else:
    # Cast as integers
    m[x].as_long()