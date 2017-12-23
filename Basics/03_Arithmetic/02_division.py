# Division support in Z3
# 
# Use: 
#    python division.py 
# 
 
from z3 import *

a = BitVec('a', 32)
r1, r2, r3, r4, r5, r6 = BitVecs('r1 r2 r3 r4 r5 r6', 32)
b, c = Reals('b c')

s = Solver()

# Z3 also has support for division: integer division, modulo, and remainder operators
# Internally they are mapped to multiplication

# In SMTLIB2, Z3 support following keyword:
#   div, mod, rem
# In Z3Py, the following mapping is done:
#   div => UDiv, SDiv    (for unsigned and signed div respectively)
#   mod => %
#   rem => URem, SRem    (for unsigned and signed rem respectively)

s.add(a == 10)

# Unsigned operations
s.add(r1 == UDiv(a, 4))     # integer division
s.add(r2 == a % 4)          # modulo
s.add(r3 == URem(a, 4))     # remainder

# Signed operations
s.add(r4 == a / -4)    # integer division
s.add(r5 == a % -4)         # modulo
s.add(r6 == SRem(a, -4))    # remainder

s.add(b >= (c / 3.0))
s.add(c >= 20.0)

print(s.check())
print(s.model())

# Division by zero is allowed, but the result is not specified.
# Division is not a partial function. All functions are total, although the result may be
# underspecified in some cases like division by zero.

s.reset()

f = a/0.0 == 10.0
print("Division by zero: {}".format(f))
s.add( f )
print(s.check())