# Solution

## Rules
- Matrix come in the form of columns * row.

## Example
Let's consider M1 and M2, two matrix of different dimension.
We will only be able to multiply M1 * M2 if and only if:
	- The number of columns of M1 (n) is the same as the number of rows of M2.
Therefore:

	 M1       M2

	(1 2)   (1 2 3)   (c11 c12 c13)
	(4 5) * (0 5 2) = (c21 c22 c23)
	(7 8)             (c31 c32 c33)
	             ___________
	            |           |
	3 x 2 = 2 x 3       3 x 3
	|   |____|           |
	|____________________|


## Input of the matrix
Each matrix will be inputed as a set of three values:
- columns
- rows

if:
	The combination of columns to rows respectively related to both matrixes does not follow the condition mentioned above a message will be outputed.
Else:
	It will be stored in an array with its dimension being the number of columns.

## Procedure
- We multiply M1's rows indices by M2's columns indices
- Then we sum the respective multiplications:
	
	1 * 1 + 2 * 0 = 1
	c11 = 1

- We then create the new matrix of dimension M1(rows) x M2(columns)


## Important functions
* List Multiplier:
	- Each list will be contained in an array
	- input: 2 lists of the same length
	- e.g.: [1, 2, 3] and [3, 4, 5]
	- result = 1 * 3 + 2 * 4 + 3 * 5
	- output: number

* Transpose Matrix:
	- As we multiply lists inside of arrays, these lists must be of equal length
	- Respecting the condition of multiplication, we will transpose the first matrix
	- e.g.: [[1, 4, 7], [2, 5, 8]]
	- output: [[1, 2], [4, 5], [7, 8]]

* Matrix Creator:
	- Create a new matrix with the solution
	- Iterate through the transposed matrix
	- Within every element of M1(transposed) -> iterate every element in M2
	- Therefore every element in M1 will respectively interact will every element in M2
	- output: matrix solution



# Front
## Window 1:
Set the dimensions of the matrix in order to create the columns and rows for the input.

## Window 2:
Create the matrix and let the user set the values for each position, e.g.: (row 1, column 1) = 3.
- Button to do the calculation





	