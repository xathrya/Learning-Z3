# Solving and manipulate the output to be displayed
# 
# Use: 
#    python iomanip.py 
# 

from z3 import *

x = Real('x')
y = Real('y')

# In default setting, all result tend to be preserved as is.
# => [x = 1/8, y = 2]
solve(x**2 + y**2 > 3, x**3 + y < 5)

# This will make all rational interpreted to decimal format
# => [x = 0.125, y = 2]
print("convert the rational representation into decimal")
set_option(rational_to_decimal=True)
solve(x**2 + y**2 > 3, x**3 + y < 5)

# Set the precision to 30 decimal place
# => [x = 0.125, y = 2]
print("Solving and displaying result with 30 decimal places")
set_option(precision=30)
solve(x**2 + y**2 > 3, x**3 + y < 5)

