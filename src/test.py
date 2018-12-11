#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:01:32 2018

@author: sufu
"""

import numpy as np


def findLegalMoves(chessboard, x, y, piece):
    moves = [[0 for col in range(8)] for row in range(8)]
    if piece == 'rook':
        moves = findHorizontalMoves(chessboard, x, y, moves)
        moves = findVerticalMoves(chessboard, x, y, moves)
    elif piece == 'bishop':
        moves = findDiagonalMoves(chessboard, x, y, moves)

    elif piece == 'queen':
        moves = findHorizontalMoves(chessboard, x, y, moves)
        moves = findVerticalMoves(chessboard, x, y, moves)
        moves = findDiagonalMoves(chessboard, x, y, moves)

    elif piece == 'horse':
        moves = findKnightMoves(chessboard, x, y, moves)
    print(piece)
    print(np.matrix(moves))


    result = list()
    for i in range(8):
        for j in range(8):
            if moves[i][j] == 1:
                result.append((i,j))

    return result

def findKnightMoves(chessboard, x, y, moves):
    try:
        moves[x+1][y+2] = 1
    except IndexError:
        pass
    try:
        if y-2 >= 0:
            moves[x+1][y-2] = 1
    except IndexError:
        pass

    try:
        moves[x+2][y+1] = 1
    except IndexError:
        pass
    try:
        if y-1 >= 0:
            moves[x+2][y-1] = 1
    except IndexError:
        pass

    try:
        if x-1 >= 0:
            moves[x-1][y+2] = 1
    except IndexError:
        pass
    try:
        if x-1 >= 0 and y-2 >= 0:
            moves[x-1][y-2] = 1
    except IndexError:
        pass

    try:
        if x-2 >= 0:
            moves[x-2][y+1] = 1
    except IndexError:
        pass
    try:
        if x-2 >=0 and y-1 >= 0:
            moves[x-2][y-1] = 1
    except IndexError:
        pass


    return moves

def findHorizontalMoves(chessboard, x, y, moves):
    for i in range(x, -1, -1):
        moves[i][y] = 1
        if chessboard[i][y] == 1:
            break
    for i in range(x, 8):
        moves[i][y] = 1
        if chessboard[i][y] == 1:
            break
    return moves


def findVerticalMoves(chessboard, x, y, moves):
    for i in range(y, -1, -1):
        moves[x][i] = 1
        if chessboard[x][i] == 1:
            break
    for i in range(y, 8):
        moves[x][i] = 1
        if chessboard[x][i] == 1:
            break
    return moves

def findDiagonalMoves(chessboard, x, y, moves):
    for i in range(8):
        try:
            moves[x+i][y+i] = 1
            if chessboard[x+i][y+i] == 1:
                break
        except IndexError:
            break

    for i in range(8):
        try:
            if y-i >= 0:
                moves[x+i][y-i] = 1
                if chessboard[x+i][y-i] == 1:
                    break
            else:
                break
        except IndexError:
            print(i)
            break;
    for i in range(8):
        try:
            if x-i >= 0:
                moves[x-i][y+i] = 1
                if chessboard[x-i][y+i] == 1:
                    break
            else:
                break
        except IndexError:
            break

    for i in range(8):
        try:
            if x-i >=0 and y-i >=0:
                moves[x-i][y-i] = 1
                if chessboard[x-i][y-i] == 1:
                    break
            else:
                break
        except IndexError:
            break
    return moves
