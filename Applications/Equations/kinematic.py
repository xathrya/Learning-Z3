# Solving kinematics equations with Z3
#
# Use: 
#    python kinematic.py 
#
from z3 import *

# Find unknown parameters in equation if other parameters are given

# d = distance, a = acceleration, t = time, v_i = initial velocity, v_f = final velocity
d, a, t, v_i, v_f = Reals('d a t v_i v_f')

# Kinetic equation
equations = [ 
    d == v_i * t + (a*t**2)/2, 
    v_f == v_i + a*t 
]

def solve_kinematic(num, problem):
    print("Problem: {}".format(problem))
    print("Solution for {}: ".format(num))
    solve(equations + problem)
    print()


print("Kinematic equations:")
print(equations)

"""
Problem 00
A van is crossing the highway with relative velocity of 30m/s. An incident occur so it
is slowing down at the rate of 8m/s2
How long it takes to make the van stop completely?

Find the value of a!
"""
problem = [ v_i == 30, v_f == 0, a == -8 ]
solve_kinematic("00", problem)

"""
Problem 01
An airplane accelerate on a runway at 3.20 m/s2 for 32.8s until finally lifts off the ground.
Determine the distance traveled before takeoff

Find the value of d!
"""
problem = [ a == 3.20, t == 32.8, v_i == 0 ]
solve_kinematic("01", problem)

"""
Problem 02
A car starts from rest and accelerates uniformly over a time of 5.21 seconds for a distance of 110 m. Determine the acceleration of the car.

Find the value of a!
"""
problem = [ d == 110, t == 5.21, v_i == 0 ]
solve_kinematic("02", problem)

"""
Problem 03
Satria is riding the Drop Tower.
If Satria free falls for 2.60 seconds, what will be his final velocity and how far will he fall?

Find the value of v_f!
"""
problem = [ t == 2.60, v_i == 0, a == 9.80 ]
solve_kinematic("03", problem)

"""
A race car accelerates uniformly from 18.5 m/s to 46.1 m/s in 2.47 seconds. Determine the acceleration of the car and the distance traveled.
"""
problem = [ t == 2.47, v_f == 46.1, v_i == 18.5 ]
solve_kinematic("04", problem)

"""
A feather is dropped on the moon from a height of 1.40 meters.
The acceleration of gravity on the moon is 1.67 m/s2.
Determine the time for the feather to fall to the surface of the moon.
"""
problem = [ a == 1.67, d == 1.40, t >= 0, v_i == 0 ]
solve_kinematic("05", problem)

"""
Rocket-powered sleds are used to test the human response to acceleration.
If a rocket-powered sled is accelerated to a speed of 444 m/s in 1.83 seconds,
then what is the acceleration and what is the distance that the sled travels?
"""
problem = [ v_f == 444, v_i == 0, t == 1.83 ]
solve_kinematic("06", problem)

"""
A bike accelerates uniformly from rest to a speed of 7.10 m/s over a distance of 35.4 m.
Determine the acceleration of the bike.
"""
problem = [ v_f == 7.10, d == 35.4 ]
solve_kinematic("07", problem)

"""
An engineer is designing the runway for an airport.
Of the planes that will use the airport, the lowest acceleration rate is likely to be 3 m/s2.
The takeoff speed for this plane will be 65 m/s.
Assuming this minimum acceleration, what is the minimum allowed length for the runway?
"""
problem = [ a == 3, v_f == 65 ]
solve_kinematic("08", problem)

"""
A car traveling at 22.4 m/s skids to a stop in 2.55 s.
Determine the skidding distance of the car (assume uniform acceleration).
"""
problem = [ v_i == 22.4, t == 2.55, v_f == 0 ]
solve_kinematic("09", problem)
