def input_matrix(c):
    matrix = []
    for i in range(c):
        row = []
        for j in range(c):
            value = float(input(f"Masukkan elemen [{i+1}, {j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix
