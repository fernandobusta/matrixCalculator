#!/usr/bin/env python3

# Logic of the process

# Matrix for testing -> m1 * m2
m1 = [[1, 4, 7], [2, 5, 8]]
m2 = [[1, 0], [2, 5], [3, 2]]

# Denote variables
m1_columns = len(m1) #2
m1_rows = len(m1[0]) #3

m2_columns = len(m2) #3
m2_rows = len(m2[0]) #2

# Verify it can be multiplied
assert(m1_columns == m2_rows)

# Functions
def list_multiplier(l1, l2):
	n = 0
	for i in range(len(l1)):
		n += (l1[i] * l2[i])
	return n

def transpose_matrix(m):
	# Create array - dimension = len(m[0])
	mt = []
	for i in range(len(m[0])):
	    mt.append([])

	for i in m:
		for j in range(len(i)):
			mt[j].append(i[j])
	return mt

def matrix_creator(mt, m2):
	newm = []
	for i in range(len(m2)):
		newm.append([])

	counter = 0
	for row_mt in mt:
		for row_m2 in m2:
			n = list_multiplier(row_mt, row_m2)
			newm[counter].append(n)
		counter += 1

	return newm

# Sends every respective column(list) to the multiplier



mt = transpose_matrix(m1)
newm = matrix_creator(mt, m2)

# Print format

for row in newm:
	print('({}  {}  {})'.format(row[0], row[1], row[2]))





