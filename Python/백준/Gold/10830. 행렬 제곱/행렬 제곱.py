import sys

input = sys.stdin.readline
n, b = map(int, input().split())
#b가 최대면 37번 나눠야됌.
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix_len = len(matrix)

for i in range(matrix_len):
    for j in range(matrix_len):
        matrix[i][j] %= 1000

#print(matrix)


#시간복잡도는 625
def matrix_mul(matrix_a, matrix_b):
    res = [[0 for _ in range(matrix_len)] for _ in range(matrix_len)]
    for r in range(matrix_len):
        for c in range(matrix_len):
            for l in range(matrix_len):
                res[r][c] += matrix_a[r][l] * matrix_b[l][c]
            res[r][c] %= 1000
    return res


def div_con(i):
    if i == 1:
        return matrix

    temp = div_con(i // 2)
    if i % 2 == 0:
        res = matrix_mul(temp, temp)
    else:
        res = matrix_mul(matrix_mul(temp, temp), matrix)

    return res


# ans = matrix_mul(matrix, matrix)
# for i in ans:
#     print(*i)
ans = div_con(b)
for i in ans:
    print(*i)
