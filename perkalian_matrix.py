def perkalian(m1, m2):
    result = [[0 for _ in range(4)] for _ in range(4)]
    
    for i in range(4):
        for j in range(4):
            result[i][j] = sum(m1[i][k] * m2[k][j] for k in range(4))
    
    return result