#!/usr/bin/python3

import sys

def print_solution(board):
    if any(1 in x for x in board):
        print([[idx, board[idx].index(1)] for idx, val in enumerate(board)])


def is_square_safe(row, col, board, n, diags):
    if board[row][col]:
        return False
    if col - diags >= 0 and board[row][col - diags]:
        return False
    if col + diags < (n) and board[row][col + diags]:
        return False
    if row == 0:
        return True
    return is_square_safe(row - 1, col, board, n, diags + 1)


def place_queen(row, col, board, n):
    for c in range(col, n):
        if 1 in board[row]:
            return 0
        if not is_square_safe(row - 1, c, board, n, 1):
            continue
        board[row][c] = 1
        return
    return 1


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

n = sys.argv[1]

if not str.isdigit(n):
    print("N must be a number")
    sys.exit(1)

n = int(n)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = 0

while queen != n:
    board = [[0 for x in range(n)] for x in range(n)]
    board[0][queen] = 1
    col = 0
    row = 1
    while row < n:
        if place_queen(row, col, board, n):
            row -= 1
            col = board[row].index(1)
            board[row][col] = 0
            col += 1
            if not row:
                break
        else:
            row += 1
            col = 0
    print_solution(board)
    queen += 1
