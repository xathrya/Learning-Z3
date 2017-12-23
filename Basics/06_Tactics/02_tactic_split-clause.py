# Tactics introduction: split-clause
#
# Use: 
#    python tactic_split-clause.py 
# 
from z3 import *

# see tactic.py

# Tactic split-clause will select a clause Or(f_1, ..., f_n) in the input goal
# and split it n subgoals

x, y = Reals('x y')
g = Goal()

g.add(Or(x < 0, x > 0), x == y + 1, y < 0)

t = Tactic('split-clause')
r = t(g)
for g in r:
    print(g)

