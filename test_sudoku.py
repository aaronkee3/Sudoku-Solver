from sudoku import Sudoku
import pytest

board = [[0, 5, 0, 3, 0, 0, 0, 2, 1],
        [0, 0, 1, 5, 0, 9, 0, 0, 7],
        [0, 0, 2, 8, 7, 0, 0, 6, 0],
        [6, 8, 0, 0, 0, 3, 0, 0, 0],
        [1, 9, 0, 7, 8, 2, 5, 0, 6],
        [7, 0, 0, 9, 0, 0, 0, 0, 4],
        [5, 0, 8, 6, 0, 7, 0, 1, 0],
        [2, 0, 0, 0, 9, 0, 4, 5, 3],
        [3, 1, 9, 2, 0, 5, 0, 0, 0]]

game = Sudoku()
game._board = board

def test_checkBox():
    for i in range(3):
        for j in range(3):
            assert game.checkBox(1, i, j) == True
            assert game.checkBox(2, i, j) == True
            assert game.checkBox(3, i, j) == False
            assert game.checkBox(4, i, j) == False
            assert game.checkBox(5, i, j) == True
            assert game.checkBox(6, i, j) == False
            assert game.checkBox(7, i, j) == False
            assert game.checkBox(8, i, j) == False
            assert game.checkBox(9, i, j) == False
    
    
def test_checkRow():
    assert game.checkRow(1, 0) == True
    assert game.checkRow(1, 1) == True
    assert game.checkRow(1, 2) == False

    assert game.checkRow(2, 3) == False
    assert game.checkRow(2, 4) == True
    assert game.checkRow(2, 5) == False

def test_checkCol():
    assert game.checkCol(2, 0) == True
    assert game.checkCol(2, 1) == False
    assert game.checkCol(2, 2) == True

    assert game.checkCol(3, 3) == True
    assert game.checkCol(3, 4) == False
    assert game.checkCol(3, 5) == True
    
def test_isValid():
    assert game.isValid(1, 0, 0) == False
    assert game.isValid(2, 0, 0) == False
    assert game.isValid(3, 0, 0) == False
    assert game.isValid(4, 0, 0) == True
    assert game.isValid(5, 0, 0) == False
    assert game.isValid(6, 0, 0) == False
    assert game.isValid(7, 0, 0) == False
    assert game.isValid(8, 0, 0) == True
    assert game.isValid(9, 0, 0) == True