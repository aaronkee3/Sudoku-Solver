from flask import Flask, flash, redirect, render_template, request, session
from sudoku import Sudoku


app = Flask(__name__)

@app.route("/")
def index():
    

    return render_template("index.html")

#maybe can add in memoitization to speed up the solve
@app.route("/solveSudoku", methods=["POST"])
def solveSudoku():
    game = Sudoku()
    board = [["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9"],
            ["s10", "s11", "s12", "s13", "s14", "s15", "s16", "s17", "s18"],
            ["s19", "s20", "s21", "s22", "s23", "s24", "s25", "s26", "s27"],
            ["s28", "s29", "s30", "s31", "s32", "s33", "s34", "s35", "s36"],
            ["s37", "s38", "s39", "s40", "s41", "s42", "s43", "s44", "s45"],
            ["s46", "s47", "s48", "s49", "s50", "s51", "s52", "s53", "s54"],
            ["s55", "s56", "s57", "s58", "s59", "s60", "s61", "s62", "s63"],
            ["s64", "s65", "s66", "s67", "s68", "s69", "s70", "s71", "s72"],
            ["s73", "s74", "s75", "s76", "s77", "s78", "s79", "s80", "s81"]]
    for row in range(9):
        for col in range(9):
            square = request.form.get(board[row][col])
            if square == "":
                square = 0
            else:
                square = int(square)
            game.setSquare(row=row, col=col, value=square)

    game.solve()

    for row in range(9):
        for col in range(9):
            board[row][col] = game.solvedBoard()[row][col]


    return render_template("solveSudoku.html", board=board)

@app.route("/completed")
def completed():
    return render_template("completed.html")