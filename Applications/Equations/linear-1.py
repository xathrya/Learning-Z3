# A linear programming with Z3
#
# Use: 
#    python linear.py 
#
from z3 import *
# example of http://en.wikipedia.org/wiki/Linear_programming

# initial conditions
A = 100
F = 500; Fs = [19, 22]
P = 260; Ps = [16, 13]
Ss = [600, 480]

# return (satisfiability, model)
def maximize(s, v):
    # Determine initial lower
    r = s.check()
    if r != sat:
        return r, None
    m = s.model()
    lower = m[v].as_long()

    # Find upper
    upper = lower + 128
    while True:
        s.push()
        s.add(v >= upper)
        r = s.check()
        s.pop()
        if r == unsat:
            break
        elif r == unknown:
            return unknown, None
        m = s.model()
        lower, upper = upper, upper + (upper - lower) * 2

    # max in [lower, upper)
    while upper - lower > 1:
        mid = (lower + upper) / 2
        s.push()
        s.add(v >= mid)
        r = s.check()
        s.pop()
        if r == sat:
            lower = mid
            m = s.model()
        elif r == unsat:
            upper = mid
        else:
            return unknown, None
    return sat, m


xs = IntVector("x", 2)
v = Int("value")

s = Solver()
# maximize variable
s.add(v == Ss[0]*xs[0] +Ss[1]*xs[1])
# constraints
s.add(xs[0] + xs[1] <= A)
s.add(Fs[0]*xs[0] + Fs[1]*xs[1] <= F)
s.add(Ps[0]*xs[0] + Ps[1]*xs[1] <= P)
s.add(xs[0] >= 0, xs[1] >= 0)

r, m = maximize(s, v)
print(r, m)