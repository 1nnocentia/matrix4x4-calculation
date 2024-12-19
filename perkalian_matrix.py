def perkalian(m1, m2 , c):
    result = [[0 for _ in range(c)] for _ in range(c)]
    
    for i in range(c):
        for j in range(c):
            result[i][j] = sum(m1[i][k] * m2[k][j] for k in range(c))
    
    return result