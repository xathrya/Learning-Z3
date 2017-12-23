# All operator used in Z3 (and Z3Py)
# 
# Use: 
#    python operator.py 
# 
 
from z3 import *

a, b, c = Ints('a b c')
p, q, r = Bools('p q r')
k, l, m = BitVecs('k l m', 16)

# a, b, and c has distinct value.
solve(Distinct(a, b, c))

# The expression/formula are not immediately evaluated
# In other words, Z3 will build an AST representation


#### Arithmetic operator
#   +  (addition)
#   -  (subtract)
#   *  (muliply)
#   ** (power)
#   /  (divide)
#   %  (modulo/remainder)
add1 = a + b 
sub1 = a - b
mul1 = a * b
pwr1 = a ** b
div1 = a / b 
mod1 = a % b


#### Comparison operator
# Signed operation
#   <  (less than)
#   >  (greater than)
#   <= (less-than or equal)
#   >= (greater-than or equal))
# Unsigned operation (at least one component is bitvector)
#   ULT (less than)
#   UGT (greater than)
#   ULE (less-than or equal)
#   UGE (greater-than or equal)
# Other comparison operation
#   != (not equal)
#   == (equality)
op1 = b < c
op2 = b > c 
op3 = b <= c
op4 = b >= c 

# Note: Unlike math, we cannot create a comparison in form like this:
#       a < b < c
# Instead, separate it to two comparison
#       a < b, b < c

# unsigned operation only works if at least one component is bitvector (section 02_bits)
op5 = ULT(k, l)
op6 = UGT(k, l) 
op7 = ULE(k, l) 
op8 = UGE(k, l)

op9  = a == c
op10 = a != c


#### Logical operator
#   And           (AND)
#   Or            (OR)
#   Not           (NOT)
#   Xor           (XOR)
#   Implication   (=>)
#   Biimplication (==)

# (a = b) and (b = c)
exp1 = And(a == b, b == c)
solve(exp1)

# or something like this is equal to AND-ing all subexpression
x = [a == b, b == c]
solve(And(x))

# (a = b) or (b = c)
y = [a == b, b == c]
solve(Or(y))

qq = Not(q)

# Built-in implies operator on Z3
#   p => q
#   r = ~q
#   ~p v r
solve(Implies(p,q), r == Not(q), Or(Not(p), r))