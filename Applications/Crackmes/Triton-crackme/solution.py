# Using Z3 to solve a crackme
#
# Use: 
#    python solution.py 
# 

from z3 import *

s = Solver()

pass   = IntVec('pass', 11)
errors = Int('errors')

passval1 = (pass[0]-pass[10])
passval2 = (pass[1]-pass[9])
passval3 = (pass[2]-pass[8])
passval4 = (pass[3]-pass[7])
passval5 = (pass[4]-pass[6])
passval6 = (pass[9]-pass[5])

# Constraint 1 (passval2 - passval4 != 0)
s.add(passval2 - passval4 != 0)

# Constraint 2 (passval1 - passval5 != 0)
s.add(passval1 - passval5 != 0)

# Constraint 3 (passval3 - passval6 != 0)
s.add(passval3 - passval6 != 0)



# Last check
~((pass[0]<<1)&0xFF)&0xFF + errors -1 == 0x58 
~((pass[errors]<<1)&0xFF)&0xFF + 3*errors - 3 == 192