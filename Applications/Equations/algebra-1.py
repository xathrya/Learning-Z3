# Solving algebra equations with Z3
#
# Use: 
#    python algebra.py 
# 
from z3 import *

## Common functions
#  Print solution of particular problem
def print_solution(problem, solver):
    print("Solution to problem %s: " % problem)
    if solver.check() == sat:
        model = solver.model()
        print(model)
        for v in model:
            print("* %s = %s" % (v, model[v]))
    else:
        print("* Can't solve the problem")

#  Make following expression have absolute value as constraint
def declare_abs(solver, var, expr):
    solver.add(Or(
        And(var == expr, expr >= 0),
        And(var == -expr, expr <= 0)
    ))

#  Compute a distance of two points
def declare_distance(solver, a_b, ax, ay, bx, by):
    solver.add(a_b >= 0)
    solver.add(a_b**2 == (ax - bx) ** 2 + (ay-by)**2)

"""
Problem 1: Solve following equation
    5(-3x - 2) - (x - 3) = -4(4x + 5) + 13
"""
def problem_01():
    solver = Solver()
    x = Real("x")
    solver.add(5 * (-3 * x - 2) - (x - 3) == -4*(4*x + 5) + 13)
    print_solution("01", solver)

"""
Problem 3: If x < 2, simplify
    |x - 2| = 4|-6|
"""
def problem_03():
    solver = Solver()
    x = Real("x")
    xm2abs = Real("x-2")
    declare_abs(solver, xm2abs, x-2)
    m6abs = Real("|-6|")
    declare_abs(solver, m6abs, -6)
    solver.add(x < 2)
    solver.add(xm2abs == 4 * m6abs)
    print_solution("03", solver)

"""
Problem 4: Find the distance between the points (-4 , -5) and (-1 , -1).
"""
def problem_04():
    solver = Solver()
    ax = Real("ax")
    ay = Real("ay")
    bx = Real("bx")
    by = Real("by")
    a_b = Real("|a-b|")
    declare_distance(solver, a_b, ax, ay, bx, by)
    solver.add(ax == -4)
    solver.add(ay == -5)
    solver.add(bx == -1)
    solver.add(by == -1)
    print_solution("04", solver)

"""
Problem 5: Find the x intercept of the graph of the equation
    2x - 4y = 9
"""
def problem_05():
    solver = Solver()
    x = Real("x")
    y = Real("y")
    solver.add(2*x - 4*y == 9)
    solver.add(y == 0)
    print_solution("05", solver)

"""
Problem 6: Evaluate f(2) - f(1)
    f(x) = 6x + 1
"""
def problem_06():
    solver = Solver()

    def declare_f(x, y):
        solver.add(y == 6*x + 1)

    x1 = Real("x1")
    y1 = Real("y1")
    x2 = Real("x2")
    y2 = Real("y2")
    answer = Real("answer")
    solver.add(x2 == 2)
    solver.add(x1 == 1)
    declare_f(x1, y1)
    declare_f(x2, y2)
    solver.add(answer == y2 - y1)
    print_solution("06", solver)
"""
Problem 10: Solve the equation
    |-2x + 2| -3 = -3
"""
def problem_10():
    solver = Solver()
    x = Real("x")
    y = Real("|-2x + 2|")
    declare_abs(solver, y, -2 * x + 2)
    solver.add(y - 3 == -3)
    print_solution("10", solver)


problem_01()
problem_03()
problem_04()
problem_05()
problem_06()
problem_10()