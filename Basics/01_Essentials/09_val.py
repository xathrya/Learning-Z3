# Type conversion in Z3
#   - Convert python to Z3
#   - Convert Z3 type to other Z3 type
# 
# Use: 
#    python val.py 
# 

from z3 import *

x = Real('x')

# In python type-system, python recognize integer numbers as well as real numbers
# When we write expression consists of valid python expression, python will
# calculate the operation and produce some value

# There is an option to make Z3 handle the representation and keep the formula intact.

# Python consider this as raw operation, calculate the value for 1/3
# => 0.3333333333333333
print( 1/3 )

# Use Z3, convert 1 to RealVal (value of Real in Z3)
# RealVal(1)/3 will create an AST for this expression
# => 1/3
print( RealVal(1)/3 )

# A shortcut to represent Quotient or rational numbers in Z3
# => 1/3
print( Q(1,3) )

print( x + 1/3 )
print( x + Q(1,3) )
print( x + "1/3" )
print( x + 0.25 )

### Type conversion
# We can convert Python data type to Z3 types
# We have seen an example of RealVal that convert python type to Z3 reals.
# Other than that we also have.

#   Declare: IntVal(value)
#   Declare: RealVal(value)
#   Declare: BoolVal(value)

x = IntVal(135)         # create a Z3 int with 135 as value
y = RealVal(3.14)       # create a Z3 real with 3.14 as value
z = BoolVal(True)       # create a Z3 bool with True as value

# We can also convert one type to other type
#   Declare: ToReal(value)
#   Declare: ToInt(value)
x = Int('x')
y = Real('y')
xr = ToReal(x)
yi = ToInt(y)