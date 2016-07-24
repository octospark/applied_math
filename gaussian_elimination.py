def gauss_el(matrix):
    for j in range(len(matrix)):
        if matrix[j][j] == 0:
            print("A is not regular.")
	    break
	else:
            for i in range(j+1, len(matrix)):
                l = matrix[i][j] / matrix[j][j]
                row = multiply_by_scalar(-l, matrix[j])
		matrix[i] = add_row(matrix[i], row)

    return matrix

def multiply_by_scalar(a, row):
    result = []
    for i in row:
    	result.append(a * i)
    return result

def add_row(row1, row2):
    result = []
    for index, element in enumerate(row1):
    	result.append(row1[index] + row2[index])
    return result
