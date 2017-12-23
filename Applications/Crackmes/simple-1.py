from z3 import *

"""
Algorithm:
T='Fguad2x-GP5_QqNi'
key=<user input>

if len(key) != 3:
    exit(1)

out=[]
for c in key:
    out.append(T[ord(c)>>4])
    out.append(T[ord(c) & 0xf])

if ''.join(out) == '--xPxN':
    print('You win')
"""

s = Solver()

final = String('final')
nth = Function('nth', StringSort(), IntSort(), BitVecSort(8))
T_  = 'Fguad2x-GP5_QqNi'
for i,j in enumerate(T_):
    s.add(nth(final, i) == ord(j))

solution = '--xPxN'
key = [BitVec('key%d' % i, 8) for i in range(3)]

for i in range(3):
    s.add(65 <= key[i], key[i] <= 122)
    s.add(nth(final, BV2Int(key[i] >> 4))  == ord(solution[2*i]))
    s.add(nth(final, BV2Int(key[i] & 0xF)) == ord(solution[2*i+1]))

if s.check() == sat:
    print("Satisfying with model: ")
    m = s.model()
    print(m)
    print(chr(m[key[0]].as_long()))
    print(chr(m[key[1]].as_long()))
    print(chr(m[key[2]].as_long()))
else:
    print("Unsatisfied!")