def square_matrix_simple(matrix=[]):
    # Get the number of rows and columns in the input matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Create a new matrix to store the square values
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Iterate through each element of the input matrix
    for i in range(rows):
        for j in range(cols):
            # Calculate the square value and store it in the new matrix
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix