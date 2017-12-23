from z3 import *

# Queen must be in different row
# Represent each queen by a single integer.
Q = [ Int('Q%i' % (r+1) ) for r in range(8) ]

# Each queen is in a colum {1, ..., 8}
val_c = [ And(1 <= Q[i], Q[i] <= 8) for i in range(8) ]

# At most one queen per column
col_c = [ Distinct(Q) ]

# Diagonal constraints
diag_c = [ If(i == j, True, And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i)) for i in range(8) for j in range(i) ]

s = Solver()
s.add(val_c + col_c + diag_c)

total = 0
while s.check() == sat:
    m = s.model()
    for i in range(8):
        sys.stdout.write("%s " % str(m[Q[i]]))
    print("")

    blocks = []
    for el in m:
        obj = el()
        blocks.append(obj != m[el])
    s.add(Or(blocks))
    total = total + 1

print("Total = %d" % total)