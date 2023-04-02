#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox

def list_multiplier(l1, l2):
	n = 0
	for i in range(len(l1)):
		n += (l1[i] * l2[i])
	return n

def add_spaces(max_length, result):
    for row in result:
        if len(row) < max_length:
            spaces = max_length - len(row)
            row += ' ' * spaces
    return result

class Matrix(object):

	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns

	def create_arrays(self, root2):
		m = []
		

		for i in range(self.columns):
		    m.append([])
		

		for i in range(self.columns):
		    for j in range(self.rows):
		        m[i].append(Entry(root2, width=10, bg='black', borderwidth=1))

		return m

	def get_from_m(self, m):
		m_values = []
		for i in range(self.columns):
		    m_values.append([])
		for i in range(len(m)):
			for j in range(len(m[i])):
				m_values[i].append(int(m[i][j].get()))
		return m_values

	def list_multiplier(self, l1, l2):
		n = 0
		for i in range(len(l1)):
			n += (l1[i] * l2[i])
		return n

	def transpose_matrix(self, m):
		# Create array -> dimension = len(m[0])
		mt = []
		for i in range(len(m[0])):
		    mt.append([])

		for i in m:
			for j in range(len(i)):
				mt[j].append(i[j])
		return mt

	def matrix_creator(self, mt, m2):
		newm = []
		for i in range(len(m2)):
			newm.append([])

		counter = 0
		for column_m2 in m2:
			for row_m2 in mt:
				n = list_multiplier(column_m2, row_m2)
				newm[counter].append(n)
			counter += 1
		return newm

	def get_result(self, matrix_result):
		result = []
		for i in range(len(matrix_result[0])):
		    result.append([''])

		for i in range(len(matrix_result)):
		    line = ''
		    for j in range(len(matrix_result[i])):
		        result[j] += '   ' + str(matrix_result[i][j])

		    length_of_string = [len(k) for k in result] 
		    result = add_spaces(max(length_of_string), result)

		return result


		









		
