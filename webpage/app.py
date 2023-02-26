from flask import Flask, flash, redirect, render_template, request, session
import sudoku


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solveSudoku")
def solveSudoku():
    return render_template("solveSudoku.html")

@app.route("/completed")
def completed():
    return render_template("completed.html")