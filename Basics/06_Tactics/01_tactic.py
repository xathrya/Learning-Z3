# Tactics introduction
#
# Use: 
#    python tactic.py 
# 
from z3 import *

# Z3 contain many tightly integrated, handcrafted heuristic combinations of algorithmic proof methods. 
# While these heuristic combinations tend to be highly tuned for known classes of problems, 
# they may easily perform very badly on new classes of problems. 
# This issue is becoming increasingly pressing as solvers begin to gain the attention of practitioners 
# in diverse areas of science and engineering. 
# In many cases, changes to the solver heuristics can make a tremendous difference. 

# Z3 implements a methodology for orchestrating reasoning engines where "big" symbolic reasoning steps 
# are represented as functions known as `tactics`, and tactics are composed using combinators known as `tacticals`. 
# Tactics process sets of formulas called `Goals`. 

# When a tactic is applied to some goal G, four different outcomes are possible. 
#    1. The tactic succeeds in showing G to be satisfiable (i.e., feasible);
#    2. Succeeds in showing G to be unsatisfiable (i.e., infeasible); 
#    3. Produces a sequence of subgoals; 
#    4. Fails. 
# When reducing a goal G to a sequence of subgoals G1, ..., Gn, we face the problem of model conversion. 
# A model converter construct a model for G using a model for some subgoal Gi. 

# Example:
# Create a goal g consisting of three formulas
# A tactic t composed of two build-in tactics: simplify and solve-eqs

x, y = Reals('x y')
g = Goal()

g.add(x > 0, y > 0, x == y + 2)
print(g)

# Apply transformations equivalent to the ones found i the command simplify
t1 = Tactic('simplify')
# Eliminate variable using Gaussian elimination.
t2 = Tactic('solve-eqs')
# Applies the first tactice (simplify) to the goal and use second tactic (solve-eqs) to each subgoal produce by the first
t  = Then(t1, t2)
print(t(g))

