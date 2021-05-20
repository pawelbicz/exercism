def saddle_points(matrix):
    if is_matrix_empty(matrix):
        return []
    if not has_matrix_correct_shape(matrix):
        raise ValueError("incorrect matrix shape")

    saddle_points = []
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num == max(row) and num == min([row[j] for row in matrix]):
                saddle_points.append({"row": i+1, "column": j+1})
    return saddle_points


def has_matrix_correct_shape(matrix):
    shape = len(matrix[0])
    for row in matrix:
        if shape != len(row):
            return False
    return True


def is_matrix_empty(matrix):
    if matrix == []:
        return True
    return False

