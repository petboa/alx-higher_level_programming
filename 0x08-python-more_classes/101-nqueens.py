#!/usr/bin/python3

import sys


def print_solution(board):
    if any(1 in x for x in board):
        print([[idx, board[idx].index(1)] for idx, val in enumerate(board)])


def is_square_safe(row, col, board, n):
    for i in range(row):
        if board[i][col]:
            return False
        if col-(row-i) >= 0 and board[i][col-(row-i)]:
            return False
        if col+(row-i) <= n-1 and board[i][col+(row-i)]:
            return False
    return True


def solve_n_queens(n):
    queen_cols = [-1] * n
    board = []
    for i in range(n):
        board.append([0]*n)
    queen = 0
    col = 0
    while queen >= 0:
        while col < n:
            if is_square_safe(queen, col, board, n):
                board[queen][col] = 1
                queen_cols[queen] = col
                queen += 1
                col = 0
                break
            else:
                col += 1
        if col == n or queen == n:
            if queen == n:
                print_solution(board)
            queen -= 1
            col = queen_cols[queen] + 1
            queen_cols[queen] = -1
            board[queen][col-1] = 0
    return


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

solve_n_queens(n)
print("OK")
