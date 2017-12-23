from z3 import *
import sys
import time

# Example:
#
#        9
#      6  15
#   10  16   1
# 13   3  19  20
#
# Seperti segitiga pascal, tapi nilai blok merupakan selisih dari 2 blok di bawahnya.
# Challenge: semua angka harus unik / hanya boleh muncul sekali
# Cari yang selisih antara nilai max dan nilai min paling kecil.
# 
# Ref: http://www.recmath.org/contest/Triangles/TriangleSpans.html

def abs(x):
    return If(x >= 0, x, -x)

ROW = 13
N   = int((1 + ROW) * ROW / 2)

# 32-bit integers is enough (?)
pascal = [ BitVec('pascal{}'.format(i), 32) for i in range(N) ]

solver = Solver()

## Building constraint
# only positive numbers
for p in pascal:
    solver.add(0 < p, p < 300)

# all numbers are distinct
solver.add(Distinct(pascal))

# value of current node is different between two node below
idx = 0
for i in range(ROW - 1):
    for j in range(i+1):
        solver.add( pascal[idx] == abs( pascal[ idx + i + 1 ] - pascal[ idx + i + 2 ] ) )
        idx += 1

# Constraint solve
start_time = time.time()
if solver.check() == sat:
    model = solver.model()

    pascal_int = list(map(lambda c: model[c].as_long(), pascal))
    pascal_min = min(pascal_int)
    pascal_max = max(pascal_int)

    idx = 0
    for i in range(ROW):
        for j in range(i + 1):
            sys.stdout.write("{} ".format(pascal_int[idx]))
            idx += 1
        print("")

    print("Deret: {}".format(pascal_int[-ROW:]))
    print("Nilai minimum: {}".format(pascal_min))
    print("Nilai maximum: {}".format(pascal_max))
    print("Selisih max dan min: {}".format(pascal_max-pascal_min))
else:
    print("No solution!")
print("Execution done in {} s".format(time.time() - start_time))

