def minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in m[:i] + m[i + 1:]]