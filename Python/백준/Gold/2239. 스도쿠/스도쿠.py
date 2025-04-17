blanks = []
board = []

row_check = [[False for _ in range(10)] for _ in range(9)]
col_check = [[False for _ in range(10)] for _ in range(9)]
box_check = [[[False for _ in range(10)] for _ in range(3)] for _ in range(3)]
def can_pos(row, col, n):
    if row_check[row][n]:
        return False
    if col_check[col][n]:
        return False
    if box_check[row // 3][col // 3][n]:
        return False

    return True


for i in range(9):
    temp = input()
    temp = [int(i) for i in temp]
    for j in range(9):
        if temp[j] == 0:
            blanks.append((i, j))
        else:
            row_check[i][temp[j]] = True
            col_check[j][temp[j]] = True
            box_check[i // 3][j // 3][temp[j]] = True
    board.append(temp)

def search(k):
    if k == len(blanks):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end="")
            print()
        exit()

    r, c = blanks[k][0], blanks[k][1]

    for i in range(1, 10):
        if can_pos(r, c, i):
            row_check[r][i] = True
            col_check[c][i] = True
            box_check[r // 3][c // 3][i] = True
            board[r][c] = i
            search(k + 1)
            row_check[r][i] = False
            col_check[c][i] = False
            box_check[r // 3][c // 3][i] = False



search(0)