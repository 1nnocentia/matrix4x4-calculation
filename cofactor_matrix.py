from determinant_matrix import determinant
from minor_matrix import minor

def cofactor(m, c):
    cofactors = [[0] * c for _ in range(c)]
    for i in range(c):
        for j in range(c):
            minor_matrix = minor(m, i, j)
            cofactors[i][j] = ((-1) ** (i + j)) * determinant(minor_matrix)
    return cofactors