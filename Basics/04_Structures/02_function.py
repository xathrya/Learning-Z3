# Introducing Function
# 
# Use: 
#    python function.py 
# 

from z3 import *

x, y = Ints('x y')
z    = Real('z')

# Unlike programming languages where functions have side effects, can throw exceptions
# or never return, functions in classical first order logic have no side-effects and
# are `total`. That is, they are defined on all input values.
# Function and constant symbols in pure first-order logic are uninterpreted or free.
# It means that no a priori interpretation is attached.
# This is contrast to functions belonging to the signature of theories, such as arithmetic
# where the function + has a fixed standard interpretation (it adds two numbers)
# Uninterpreted functions and constants are maximally flexible, they allow any interpretation
# that is consistent with the constraints over the function or constant.

# Define a function (Application function)
# Function('name', Arg1Sort(), Arg2Sort(), ..., RetValSort())
# Function f with 1 argument of Int and return Int
f = Function('f', IntSort(), IntSort())
# Function g with 2 argument of Int and return Int
g = Function('g', IntSort(), IntSort(), IntSort())

# Take a look at f and g
print("Dissecting f")
print("f.name():   {}".format(f.name()))
print("f.range():  {}".format(f.range()))
print("f.arity():  {}".format(f.arity())) 
for i in range(f.arity()):
    print("domain({}): {}".format(i, f.domain(i)))

print()

print("Dissecting g")
print("g.name():   {}".format(g.name()))
print("g.range():  {}".format(g.range()))
print("g.arity():  {}".format(g.arity())) 
for i in range(g.arity()):
    print("domain({}): {}".format(i, g.domain(i)))

print()

# Trying to interpret a function based on constraint
solve(f(f(x)) == x, f(x) == y, x != y)
# [x = 0, y = 1, f = [0 -> 1, 1 -> 0, else -> 1]]
# with x = 0 and y =1 we can interpret f as such
# f(0) is 1
# f(1) is 0
# f(a) is 1 for all a different from 0 and 1

# evaluate expression in the model for a system of constraints
s = Solver()
s.add(f(f(x)) == x, f(x) == y, x != y)
print(s.check())
m = s.model()
print("f(f(x)) = {}".format(m.evaluate(f(f(x)))))
print("f(x)    = {}".format(m.evaluate(f(x))))
print("f(3)    = {}".format(m.evaluate(f(3))))