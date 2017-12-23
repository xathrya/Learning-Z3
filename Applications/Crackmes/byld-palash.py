# Crack the byld's palash crackme
#
# Use: 
#    python byld-palash.py 
# 
from z3 import *
import os

## The code
#
#    for ( i = 0; i <= 9; ++i )
#    {
#        v2 += 53 * v6[i];
#        v3 += ((((v2 >> 32) >> 25) + v2) & 0x7F)
#            - ((v2 >> 32) >> 25)
#            + *(creds2 + 8)[i];
#        v4 += (23 * (v6[v3 % 13] - 48) + 32) % 30 ^ kk2[i];
#    }
#    result = v4 == 0;
#}

solver = Solver()

for i in range(0, 10):
    globals()['b%i' % i] = BitVec('b%i' % i, 32)
    # Ensure only ASCII input
    solver.add(globals()['b%i' % i] >= 48)
    solver.add(globals()['b%i' % i] <= 122)

I = Array('kk2',BitVecSort(32), BitVecSort(32))
kk2 = [25,18,4,4,4,2,18,20,20,6]
for i in range(0, len(kk2)):
    solver.add(I[i] == kk2[i])

J = Array('e',BitVecSort(32), BitVecSort(32))
e = [49, 56, 52, 48, 51, 57, 54, 53, 52, 56, 57, 50, 52]
for i in range(0, len(e)):
    solver.add(J[i] == e[i])

a = BitVecVal(0, 32)
b = BitVecVal(0, 32)
c = BitVecVal(0, 32)
d = BitVecVal(0, 32)
x = BitVecVal(0, 32)
for i in range(0,10):
    a += J[i] * 53
    b += ((((a >> 32) >> 25) + a) & 0x7F) - ((a >> 32) >> 25) + globals()['b%i' % i]
    d = ((J[b%13]-48) * 23 + 32) % 30
    solver.add((d ^ I[i]) == 0)
    #print solver

print("Solving...")

# Solve the equations
print(solver.check())
modl = solver.model()

# Create an ASCII string from the resulting bytes
res = ""
for i in range(0,10):
    obj = globals()['b%i' % i]
    c = modl[obj].as_long()
    print('b%i: %x' % (i, c))
    res = res + chr(c)

print("Result: " + res);