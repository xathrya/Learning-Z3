from z3 import *

def addConstraintBetweenXandY(solver, group, x, y):
	for i in range(0, len(group)):
		solver.add(group[i] >= x, group[i] < y)


def addConstraintNotEq(solver, g1, g2):
	for i in range(0,4):
		solver.add(g1[i] != g2[i])


# setting the groups of numbers
first = IntVector('a', 4)
second = IntVector('b', 4)
third = IntVector('c', 4)
fourth = IntVector('d', 4)

# creating the solver
s = Solver()


# do the sums
sum_first = first[0]+first[1]+first[2]+first[3]
sum_second = second[0]+second[1]+second[2]+second[3]
sum_third = third[0]+third[1]+third[2]+third[3]
sum_fourth = fourth[0]+fourth[1]+fourth[2]+fourth[3]

# average of groups, excluding the 4th (checksum)
avg_sums = (sum_first+sum_second+sum_third)/3

#constraint #2
addConstraintBetweenXandY(s, first, 0, 9)
addConstraintBetweenXandY(s, second, 0, 9)
addConstraintBetweenXandY(s, third, 0, 9)
addConstraintBetweenXandY(s, fourth, 3, 8)

#constraint #3.1
s.add(sum_fourth == avg_sums)

#constraint #3.2
s.add(sum_first == sum_fourth/4)

#constaint #4
s.add(sum_first != sum_second)

#constraint #5
addConstraintNotEq(s, first, fourth)

#constraint #6
addConstraintNotEq(s, second, third)

if s.check():
	m = s.model()
	#print m

	for g in [first, second, third, fourth]:
		print("{}{}{}{}".format(m[g[0]], m[g[1]], m[g[2]], m[g[3]]))