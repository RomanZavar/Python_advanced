# Напишите функцию для транспонирования матрицы


def trn_matrix():
    trans_m = [[m[j][i] for j in range(len(m))] for i in range(len(m))]
    return trans_m

m = [[12, 3, 5], [6, 7, 18], [10, 11, 15]]

print(trn_matrix())


