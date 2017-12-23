# Using crackme to crack aserial generation algorithm
#
# Use: 
#    python challenge4_0B_bQeUUGe4uLcXNqRnBBand5Yk0.py 
# 
from z3 import *
import sys

# Download challenge :: challenge4_ok.exe - https://drive.google.com/open?id=0B_bQeUUGe4uLcXNqRnBBand5Yk0

length = int(sys.argv[1])
if length < 5:
    print("Length must be more than 4!")
    exit()

# Define vars
chars = [BitVec("%i" % i, 8) for i in range(length)]

solver = Solver()
constraint = []

# All values are printable characters excluding space (33-126)
for i in range(length):
    constraint += [chars[i] >= 33, chars[i] <= 126]

# Little endian == reversed
equal = [0x30, 0x5b, 0x6f, 0x2]
for i in range(4):
    placeholder = chars[i]
    for j in range(i + 1, i + 16):
        placeholder ^= chars[j] if j < length else 0
    constraint.append(placeholder == equal[i])

# argv[2] == max key generated
for loop in range(int(sys.argv[2])):
    solver.add(constraint)
    if solver.check() == sat:
        model = solver.model()
        block = []
        pwd = list("a" * length)
        for name in model:
            pwd[int(name.__str__())] = chr(model[name].as_long())
            block.append(name() != model[name])
        print("".join(pwd))
        constraint.append(Or(block))
        solver.reset()
    else: break