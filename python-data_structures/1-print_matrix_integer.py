def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = ""

        for element in row:
            formatted_row += "{:d} ".format(element)

        print(formatted_row[:-1])