class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(i) for i in elem.split()]for elem in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [i[index-1] for i in self.matrix]

