from random import randint
import numpy as np




def main():

    board = [[0 for i in range(9)] for i in range(9)]

    box = [ #row, column
        0, #nonsensical number to fill up box 0
        {"row": 2, "column": 2}, #box 1
        {"row": 2, "column": 5},
        {"row": 2, "column": 8},
        {"row": 5, "column": 2},
        {"row": 5, "column": 5},
        {"row": 5, "column": 8},
        {"row": 8, "column": 2},
        {"row": 8, "column": 5},
        {"row": 8, "column": 8} #box 9
    ]
    # for i in range (9):
    #      for j in range(9):
    #          board[i][j] += i + 1

    # print (board[2])

    # column = [row[5] for row in board]
    # print(column)

    #iterate 9 times (for each box, start from middle box)
        #randomly put 1 into center box
    centerRow = 4
    centerCol = 4

    #this guessing algorithm gets very slow after 3rd number
    while True:
        for number in range(1, 10):
            for i in range(-3, 4, 3): #iterate row to move from boxes to boxes
                for j in range(-3, 4, 3): #iterate col
                    ranRow = randomList(-1, 1)
                    ranCol = randomList(-1, 1)
                    for rowIn in ranRow:
                        check = False
                        row = centerRow + i + rowIn
                        for colIn in ranCol:
                            col = centerCol + j + colIn

                            #check if row is occupied
                            if board[row][col] != 0:
                                continue

                            if number in board[row]:
                                continue
                            
                            column = [row[col] for row in board]
                            if number in column:
                                continue
                            
                            board[row][col] = number
                            check = True
                            break
                        if check:
                            break

        break
        # zeroCheck = True
        # for line in board:
        #     if 0 in line:
        #         zeroCheck = False
        
        # if zeroCheck:
        #     break
                
    for line in board:
        print (line)

    boardNP = np.matrix(board)
    print (boardNP)
                




 



   




#randomly put 1, into box 1

#randomly put 1 into box 2 and 3, checking for row in box 1

#randomly put 1 into box 4, checking for col in box 1

#randomly put 1 into box 5, checking for row in box 4 and col in box 2

#randomly put 1 into box 6, checking for row in box 4 and 5, col in box 3

#randomly put 1 into box 7, checking for col in box 1 and 4,

#randomly put 1 into box 8, checking for row in box 7, col in box 2 and 4

#algo: if 1 is in row or col, skip

#for line in board:
#    print (line)

def randomList(start, stop): #not sure what is the most efficient way to do this
    list = []
    randomList = []
    for i in range(start, stop + 1):
        list.append(i)
    while len(list) != 0:
        index = randint(0, len(list) - 1)
        randomList.append(list[index])
        list.pop(index)
    return randomList

main()