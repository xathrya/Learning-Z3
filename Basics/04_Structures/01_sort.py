# Introducing sort, the data types
# 
# Use: 
#    python sort.py 
# 

from z3 import *

x = Int('x')
y = Int('y')
z = Real('z')

# Sort is type, sequence of possible value of certain type.
# Every expression has a sort. 

# Retrive the sort of an expression
print("# What Sort?")
print((x + 1).sort())
print((z + 1).sort())
print((x >= 2).sort())

print()

# The equivalence is based on the AST of the expression
print("# Equivalence")
print(eq(x + y, x + y))   # True
print(eq(x + y, y + x))   # False
n = x + y
print(eq(n, x + y))       # True

# The integer variable x is not equal to the real variable x
print(eq(Int('x'), Real('x')))

print()

# Hash return a hascode for an AST node.
# if eq(n1, n2) is True then n1.hash() == n2.hash()
print("# Hash")
print((x + 1).hash())
print((1 + x).hash())
print(x.sort().hash())

print()

# Declare a constant of the given sort.
# Const(name, sort)
a = Const('a', IntSort())
c, d = Consts('a b', BoolSort())

# Int(name) and Real(name) are shorthands for Const(name, IntSort()) and Const(name, RealSort())
print("Is a of Const('a', IntSort()) equal to Int('a')?: {}".format(eq(a, Int('a'))))
print("And(c,d) of const BoolSort() is: {}".format(And(c,d)))

print() 

# Creating new sort
# Function is uninterpreted (free), but this is contrast to arithmetic operators such as + and -
# that have fixed interpretation.
# However, uninterpreted function is so flexible and allow any interpretation as long as it is
# consistent with the constraints
A     = DeclareSort('A')
x, y  = Consts('x y', A)
f     = Function('f', A, A)

s     = Solver()
s.add(f(f(x)) == x, f(x) == y, x != y)

print(s.check())
m = s.model()
print(m)
print("Interpretation assigned to A: ")
print(m[A])