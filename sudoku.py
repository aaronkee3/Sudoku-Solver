from random import randint
import numpy as np

class Sudoku:

    def __init__(self):
        #initiates a 9x9 board
        self._board = [[0 for i in range(9)] for i in range(9)]

    def __str__(self):
        _printBoard = np.matrix(self._board)
        return f"{_printBoard}"

    def newBoard(self):
        #base case -> board filled completely
        #recursive -> board not filled
        for number in range(1,2):
            self.insertNumber(number)

        self.solve()
        #backtrack algo

    #To insert a number(1-9) into board
    def insertNumber(self, number):
        centerRow = 4 #fifth row and fifth col is center of the board
        centerCol = 4

        for i in range(-3, 4, 3): #to iterate over 3x3 boxes in 9x9 board
            for j in range(-3, 4, 3):
                randomRow = self.randomList(-1, 1)
                randomCol = self.randomList(-1, 1)
                check = False #if a number is inserted into a 3x3 box, change to true
                
                for rowIndex in randomRow:
                    row = centerRow + i + rowIndex
                    if self.checkRow(number, row):
                        continue

                    for colIndex in randomCol:
                        col = centerCol + j + colIndex

                        if self._board[row][col] != 0 or self.checkCol(number, col):
                            continue

                        self._board[row][col] = number #insert number into box
                        check = True
                        break
                    
                    if check:
                        break
                        

    #Output: returns a list of consecurtive integars from start to stop randomly arranged
    def randomList(self, start, stop):
        list = []
        randomList = []
        for i in range(start, stop + 1):
            list.append(i)
        while len(list) != 0:
            index = randint(0, len(list) - 1)
            randomList.append(list[index])
            list.pop(index)
        return randomList

    #Output: Returns True if number in row
    def checkRow(self, number, row):
        if number in self._board[row]:
            return True
        else:
            return False

    #Output: Returns True if number in column
    def checkCol(self, number, col):
        for i in range (9):
            if self._board[i][col] == number:
                return True
        return False

    #Output: Returns True if number in box
    def checkBox(self, number, row, col):
        rowIndex = int(row / 3) * 3
        colIndex = int(col / 3) * 3
        for i in range (rowIndex, rowIndex + 3):
            for j in range(colIndex, colIndex + 3):
                if self._board[i][j] == number:
                    return True
        return False

    def possible(self, number, row, col):
        if not (self.checkRow(number, row)):
            if not (self.checkCol(number, col)):
                if not (self.checkBox(number, row, col)):
                    return True
        return False

    
    #backtracking algo
    #Reference: https://www.youtube.com/watch?v=G_UYXzGuqvM&ab_channel=Computerphile
    #base case -> board completely filled
    #recursive -> board not completely filled
    def solve(self):
        for row in range(9):
            for col in range(9):
                if self._board[row][col] == 0:
                    for number in range(1,10):
                        if self.possible(number, row, col):
                            self._board[row][col] = number
                            self.solve()
                            self._board[row][col] = 0
                    return


    

    
