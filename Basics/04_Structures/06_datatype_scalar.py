# Using data type as enumeration.
#
# Use: 
#    python datatype_scalar.py 
# 
from z3 import *

# see also  datatype.py

### Declare enumeration (scalar)
Color = Datatype('Color')

# Each possible value is an object of Color
Color.declare('red')
Color.declare('green')
Color.declare('blue')

# Create the data type
# Using method create() to create the actual datatype
Color = Color.create()

print("is_expr? {}".format(is_expr(Color.green)))
print("is {}? {}".format(Color.green == Color.blue, simplify(Color.green == Color.blue)))

# Let c be a constant of sort Color
c = Const('c', Color)
# Then c must be either red, green, or blue
prove(Or(c == Color.green, c == Color.blue, c == Color.red))

# Shorthand for declaration
Color, (red, green, blue) = EnumSort('Color', ('red', 'green', 'blue'))
solve(c != green, c != blue)

print()