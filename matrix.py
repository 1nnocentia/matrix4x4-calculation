from input import input_matrix
from penjumlahan_matrix import penjumlahan
from pengurangan_matrix import pengurangan
from perkalian_matrix import perkalian
from transpose_matrix import transpose
from determinant_matrix import determinant
from invers_matrix import invers

a = ''

while a != 'q':
    print('Calculator Matrix')
    print('------------------')
    c = int(input('Ukuran matrix (2/3/4): '))
    print('-------------------')
    print('Operasi Matrix apa yang ingin dilakukan?')
    print('1. Penjumlahan Matrix')
    print('2. Pengurangan Matrix')
    print('3. Perkalian Matrix')
    print('4. Transpose Matrix')
    print('5. Determinant Matrix')
    print('6. Invers Matrix')
    
    b = input('Silahkan masukkan angka operasi yang ingin dilakukan (1-6): ')
    if not b.isdigit() or not (1 <= int(b) <= 6):
        print('Maaf, pilihan tidak tersedia.')
        continue

    b = int(b)
    if b in [1, 2, 3]:
        print('Matrix 1: ')
        m1 = input_matrix(c)
        for row in m1:
            print(row)

        print('Matrix 2:')
        m2 = input_matrix(c)
        for row in m2:
            print(row)

        match b:
            case 1:
                result = penjumlahan(m1, m2)
                print('Hasil Penjumlahan Matrix:')
            case 2:
                result = pengurangan(m1, m2)
                print('Hasil Pengurangan Matrix:')
            case 3:
                result = perkalian(m1, m2, c)
                print('Hasil Perkalian Matrix:')

    else:
        print('Matrix: ')
        m = input_matrix(c)
        for row in m:
            print(row)
        match b:
            case 4:
                result = transpose(m)
                print('Transpose dari Matrix:')
            case 5:
                result = determinant(m)
                print('Determinant dari Matrix:')
            case 6:
                result = invers(m, c)
                print('Invers dari Matrix:')

    if isinstance(result, list):
        for row in result:
            print(row)
    else:
        print(f'Hasil: {result}')

    a = input('Apakah masih ingin menggunakan calculator matrix? (y=lanjut, q=keluar): ')
