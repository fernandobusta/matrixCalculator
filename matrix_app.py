#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from matrix import Matrix


def window2_test():

	# M1
	row_m1 = clicked_m1.get()
	column_m1 = clicked2_m1.get()
	# M2
	row_m2 = clicked_m2.get()
	column_m2 = clicked2_m2.get()

	if column_m1 != row_m2:
		error = messagebox.askyesno("Matrix not compatible.")
		Label(root, text=response).pack()


	root2 = Tk()
	root2.title('Input Matrix')
	root2.geometry("800x600")

	#def set_entry_matrix:
		
	def one_column(r, c):
		e = Entry(root2, width=10, bg='black', borderwidth=1)
		e.grid(row=r, column=c)

	def setDim(row, column, new_start, check):
		if check:
			counter_row = new_start
		else:
			global track
			counter_row = 0

		counter_column = 1
		count_extra = 0
		for i in range(column):
			
			for j in range(row):
				e = Entry(root2, width=10, bg='black', borderwidth=1)
				e.grid(row = counter_row, column = counter_column)
				count_extra += 1
				counter_row += 1

			counter_row -= count_extra
			counter_column += 1

		track = counter_row



	myLabel_m1 = Label(root2, text=(clicked_m1.get(),'x', clicked2_m1.get()))
	myLabel_m2 = Label(root2, text=(clicked_m2.get(),'x', clicked2_m2.get()))
	myLabel_m1.grid(row=0, column=0)
	myLabel_m2.grid(row=1, column=0)

	for i in range(row_m1):
		one_column(i + 1, 1)

	root2.mainloop()





def window2():

	# M1
	row_m1 = clicked_m1.get()
	column_m1 = clicked2_m1.get()
	# M2
	row_m2 = clicked_m2.get()
	column_m2 = clicked2_m2.get()

	rows = [row_m1, row_m2]
	columns = [column_m1, column_m2]
	#print(int(max(rows)))

	if column_m1 != row_m2:
		messagebox.showerror('Python Error', 'The number of columns of M1 has to be equal to the number of rows of M2.')

	else:
		root2 = Tk()
		root2.title('Input Matrix')
		root2.geometry("1000x200")

		

		# Creating the objects for both Matrices
		m1 = Matrix(row_m1, column_m1)
		m2 = Matrix(row_m2, column_m2)

		# Definig the dimensions
		m1_input = m1.create_arrays(root2)
		m2_input = m2.create_arrays(root2)
		
		# Setting the columns and rows on tkinter
		for i in range(len(m1_input)):
			for j in range(len(m1_input[i])):
				m1_input[i][j].grid(row=j, column=i)

		# Styling equation
		row_sign = row_m1 // 2
		sign = Label(root2, text = "*")
		sign.grid(row=row_sign, column=column_m1)
		sign = Label(root2, text="=")
		sign.grid(row=row_sign, column=column_m1 + column_m2 + 1)

		# Start from 0 + number of columns of M1
		for i in range(len(m2_input)):
			for j in range(len(m2_input[i])):
				m2_input[i][j].grid(row=j, column=i + column_m1 + 1)

		def multiply():
			# Get the data in array
			m1_value = m1.get_from_m(m1_input)
			m2_value = m2.get_from_m(m2_input)
			print(m1_value,'\n', m2_value)

			# Traspose the M1
			mt = m1.transpose_matrix(m1_value)
			print(mt)
			newm = m1.matrix_creator(mt, m2_value)

			print(newm)

			result = m1.get_result(newm)
			lines = []
			for row in result:
				lines.append('(' + (''.join(row)).lstrip() + ')')



			# Matrix output in a
			Output = Label(root2, text='\n'.join(lines), height = max(rows)*2, width = 25, bg = "light cyan", fg='black')
			#Output.insert(END, '\n'.join(result))
			Output.grid(row=0, column=column_m1 + column_m2 + 2, rowspan=max(rows))

			
			



		
		multiply = Button(root2, text="Multiply", command=multiply)
		multiply.grid(row=max(rows), column=0, columnspan=column_m1 + column_m2 + 1)


		root2.mainloop()
	



def window1():
	global clicked_m1
	global clicked2_m1
	global clicked_m2
	global clicked2_m2


	root = Tk()
	root.title('Matrix Calculator')
	root.geometry("400x200")

	#def define_matrix():
	#l = Label(root, text = "The calculation will be M1 * M2\n Enter the dimension of both matrix respectively.")
	#l.grid(row=0, column=0)

	def show_dimension():
		m1Label = Label(root, text=('M1:   ', clicked_m1.get(),'x', clicked2_m1.get()))
		m2Label = Label(root, text=('M2:   ', clicked_m2.get(),'x', clicked2_m2.get()))
		m1Label.grid(row=2, column=4)
		m2Label.grid(row=3, column=4)



	options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	# Create the variable to store the integer
	# M1
	clicked_m1 = IntVar()
	clicked2_m1 = IntVar()
	# M2
	clicked_m2 = IntVar()
	clicked2_m2 = IntVar()


	# Set the initial values for the dropdown menus
	# M1
	clicked_m1.set(options[1])
	clicked2_m1.set(options[1])
	# M2
	clicked_m2.set(options[1])
	clicked2_m2.set(options[1])


	# Create the drop dow menu for both matrix
	# M1
	l = Label(root, text = "M1")
	l.grid(row=0, column=0)
	l = Label(root, text = "rows:")
	l.grid(row=1, column=0)
	l = Label(root, text = "columns:")
	l.grid(row=1, column=2)
	drop_m1 = OptionMenu(root, clicked_m1, *options)
	drop2_m1 = OptionMenu(root, clicked2_m1, *options)
	drop_m1.grid(row=1, column=1)
	drop2_m1.grid(row=1, column=3)
	# M2
	l = Label(root, text = "M2")
	l.grid(row=2, column=0)
	l = Label(root, text = "rows:")
	l.grid(row=3, column=0)
	l = Label(root, text = "columns:")
	l.grid(row=3, column=2)
	drop_m2 = OptionMenu(root, clicked_m2, *options)
	drop2_m2 = OptionMenu(root, clicked2_m2, *options)
	drop_m2.grid(row=3, column=1)
	drop2_m2.grid(row=3, column=3)

	# Buttons
	dimensionButton = Button(root, text="Show Dimension", command=show_dimension)
	dimensionButton.grid(row=1, column=4)
	matrixButton = Button(root, text="Create Matrix", command=window2)
	matrixButton.grid(row=4, column=0, columnspan=2)

	root.mainloop()

window1()



#print(clicked2.get())






