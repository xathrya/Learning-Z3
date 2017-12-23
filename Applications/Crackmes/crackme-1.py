# A crackme solution with Z3
#
# Use: 
#    python crackme.py 
# 
from z3 import *
import sys

"""
1. serial in the format of 4 group of digits XXXX-XXXX-XXXX-XXXX
2. X is int between [0..9], except 4th group will be between [3..8]
3. 4-th group will be used as a checksum
    a. sum must be equal to the sum of first group
    b. average must be equal to average of first group 
4. sum of 1st group must be different to sum of 2nd group
5. 1st group and 4th group can't have a similar value at same index
6. 2nd group 3rd group can't have a similar int at the same index 
"""

def display_solution(model):
    for i in range(4):
        for j in range(4):
            sys.stdout.write("%d" % model[groups[i][j]].as_long())
        
        if i != 3:
            sys.stdout.write(" - ")
    print("")

s = Solver()

# 1. serial in the format of 4 group of digits XXXX-XXXX-XXXX-XXXX
groups = [ IntVector('group%d' % i, 4) for i in range(1, 5) ]

# 2. X is int between [0..9], except 4th group will be between [3..8]
for i in range(3):
    for j in range(4):
        s.add(0 <= groups[i][j], groups[i][j] < 9)
for j in range(4):
    s.add(And(3 <= groups[3][j], groups[3][j] < 9))

sum_1 = Sum(groups[0])
sum_2 = Sum(groups[1])
sum_3 = Sum(groups[2])
sum_4 = Sum(groups[3])
avg_3 = Sum(sum_1, sum_2, sum_3)/3

# 3. 4-th group will be used as a checksum
# a. sum must be equal to the average of the first 3 groups
s.add(sum_4 == avg_3)

# b. average must be equal to the sum of first group 
s.add(sum_1 == sum_4/4)

#4. sum of 1st group must be different to sum of 2nd group
s.add(sum_1 != sum_2)

#5. 1st group and 4th group can't have a similar value at same index
for i in range(4):
    s.add(groups[0][i] != groups[3][i])

#6. 2nd group 3rd group can't have a similar int at the same index 
for i in range(4):
    s.add(groups[1][i] != groups[2][i])

while s.check() == sat:
    m = s.model()
    display_solution(m)

    block = []
    for el in m:
        d = el()

        block.append(d != m[el])
    s.add(Or(block))   

