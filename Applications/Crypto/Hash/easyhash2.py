# Break the insecure hash generation algorithm
#
# Use: 
#    python easyhash2.py 
# 
from z3 import *
import sys

# The hash algorithm has a weak algorithm which can be decomposed as a series of operations

# The simple hash function consists operation of multiplication and addition
# for each elements in string
def hash_function(s):
    m = 0
    for c in s:
        m *= 31
        m += c
    return m

a, b, c, d, e, f, g = Ints('a b c d e f g')
s = Solver()

# The element should be only printable character
s.add(And(a <= ord('z'), ord('a') <= a))
s.add(And(b <= ord('z'), ord('a') <= b))
s.add(And(c <= ord('z'), ord('a') <= c))
s.add(And(d <= ord('z'), ord('a') <= d))
s.add(And(e <= ord('z'), ord('a') <= e))
s.add(And(f <= ord('z'), ord('a') <= f))
s.add(And(g <= ord('z'), ord('a') <= g))

# hash_function('xathrya') == 109387809469
print(hash_function(list(map(ord, list('xathrya')))))
s.add(hash_function([a,b,c,d,e,f,g]) == 109387809469)

print(s.check())
m = s.model()
print(m)

password = chr(m[a].as_long()) + chr(m[b].as_long()) + chr(m[c].as_long()) + chr(m[d].as_long()) + chr(m[e].as_long()) + chr(m[f].as_long()) + chr(m[g].as_long())
print(password)