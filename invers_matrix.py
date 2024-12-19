from determinant_matrix import determinant
def invers(m, c):
    det = determinant(m)
    if det == 0:
        print('Tidak ada invers matrix karena determinan = 0')
    elif c == 2:
        a, b = m[0]
        c, d = m[1]
        return [[d/det, -b/det], [-c/det, a/det]]

                

