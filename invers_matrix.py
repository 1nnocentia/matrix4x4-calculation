from determinant_matrix import determinant
from minor_matrix import minor
from transpose_matrix import transpose
from cofactor_matrix import cofactor
def invers(m, c):
    det = determinant(m)
    if det == 0:
        print('Tidak ada invers matrix karena determinan = 0')
    elif c == 2:
        a, b = m[0]
        c, d = m[1]
        return [[d/det, -b/det], [-c/det, a/det]]
    else:
        cofactors = cofactor(m,c)
        adjoint = transpose(cofactors)
        invers = [[adjoint[i][j] / det for j in range(c)] for i in range(c)]
        return invers