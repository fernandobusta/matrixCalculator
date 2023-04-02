#!/usr/bin/env python3

from tkinter import *

root = Tk()
root.title('Input Matrix')
root.geometry("800x600")

def get_from_m():

    for i in range(len(m)):
        for j in range(len(m[i])):
            m_values[i].append(m[i][j].get())


rows = 3
columns = 4
# Layout: 4 x 3 -> [[a, b, c], [a, b, c], [a, b, c], [a, b, c]]
m = []
m_values = []

for i in range(columns):
    m.append([])

for i in range(columns):
    m_values.append([])

for i in range(columns):
    for j in range(rows):
        m[i].append(Entry(root, width=10, bg='black', borderwidth=1))

for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j].grid(row=j, column=i)


matrixButton = Button(root, text="getdata", command=get_from_m)
matrixButton.grid(row=9, column=1)

root.mainloop()

print(m)
print(m_values)

