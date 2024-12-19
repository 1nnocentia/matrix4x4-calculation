def input_matrix():
    print("Masukkan elemen matriks 4x4 (16 elemen):")
    matrix = []
    for i in range(4):
        row = []
        for j in range(4):
            value = float(input(f"Masukkan elemen [{i+1}, {j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix
