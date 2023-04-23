#!/usr/bin/python3

import sys


def print_board(board):
    if any(1 in x for x in board):
        print([[idx, board[idx].index(1)] for idx, val in enumerate(board)])


def is_safe(row, square, chessboard, Nm, diags):
    if chessboard[row][square]:
        return False
    if square - diags >= 0 and chessboard[row][square - diags]:
        return False
    if square + diags < Nm and chessboard[row][square + diags]:
        return False
    if row == 0:
        return True
    return is_safe(row - 1, square, chessboard, Nm, diags + 1)


def place_square(row, position, chessboard, Nm):
    for square in range(position, Nm):
        if 1 in chessboard[row]:
            return 0
        if not is_safe(row - 1, square, chessboard, Nm, 1):
            continue
        chessboard[row][square] = 1
        return
    return 1


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

if not N.isdigit():
    print("N must be a number")
    sys.exit(1)

N = int(N)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = 0

while queen != N:
    chessboard = [[0 for x in range(N)] for x in range(N)]
    chessboard[0][queen] = 1
    position = 0
    row = 1
    while row < N:
        if place_square(row, position, chessboard, N):
            row -= 1
            position = chessboard[row].index(1)
            chessboard[row][position] = 0
            position += 1
            if not row:
                break
        else:
            row += 1
            position = 0
    print_board(chessboard)
    queen += 1
