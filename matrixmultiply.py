def matrix_multiply(a_row, a_col, b_row, b_col, a, b):
    if a_col != b_row:
        raise ValueError
    else:
        for i in range(a_row):
            for j in range(b_col):
                for k in range(a_col):
                    c[i][j] = 