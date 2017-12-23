# Operator in bit vectors
# 
# Use: 
#    python declare.py 
# 
 
from z3 import *

# Create 32-bit vectors
x, y, z = BitVecs('x y z', 32)


#### Arithmetic operator
#   +  (addition)
#   -  (subtract)
#   *  (muliply)
#   /  (divide)
#   %  (modulo/remainder)
add1 = x + y
sub1 = x - y
mul1 = x * y
div1 = x / y
mod1 = x % y


#### Comparison operator
# Signed operation
#   <  (less than)
#   >  (greater than)
#   <= (less-than or equal)
#   >= (greater-than or equal)
# Unsigned operation
#   ULT (less than)
#   UGT (greater than)
#   ULE (less-than or equal)
#   UGE (greater-than or equal)
# Other comparison operation
#   != (not equal)
#   == (equality)

# Signed operation
op1 = y < z         # (bvslt)
op2 = y > z         # (bvsgt)
op3 = y <= z        # (bvsle)
op4 = y >= z        # (bvsge)

# Unsigned operation
op5 = ULT(y, z)     # (bvult)
op6 = UGT(y, z)     # (bvugt)
op7 = ULE(y, z)     # (bvule)
op8 = UGE(y, z)     # (bvuge)

# Equality
op9  = x == z
op10 = x != z


#### Logical operator
#   And           (AND)
#   Or            (OR)
#   Not           (NOT)
#   Xor           (XOR)
#   Implication   (=>)

exp1 = And(x == y, y == z)
exp2 = Not(x == y)
exp3 = Xor(x < y, y < z)
exp4 = Implies(x == 0, y == 0)
exp0 = Or(exp1, exp2, exp3, exp4)
solve(exp0)

# or something like this is equal to AND-ing all subexpression
x = [a == b, b == c]
solve(And(x))


#### Bitwise Operations
#   &      (bit-wise AND)
#   |      (bit-wise OR
#   ~      (bit-wise NOT)
solve(x & y == ~y)

#    <<    (shift (arighmetical) left)
print(simplify( x << y ))

#    LShR  (unsigned (logical) shift right)
print(simplify( LShR(x,y) ))

#    >>    (signed (arithmetical) shift right)
print(simplify( x >> y ))

# Rotation is also supported
#    RotateLeft(number, shift)
#    RotateRight(number, shift)

print(simplify( RotateLeft(x, 2) ))
print(simplify( RotateRight(x, 2) ))

# Notes:
#    - The bit width of the "target number" and the "shift amount" must be same
#    - The shift amount is always treated as unsigned