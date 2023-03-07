# SUDOKU SOLVER
#### Description:
This project solves sudoku puzzle using a web application. It is build using python flask, HTML and CSS. The code also includes a python Sudoku class that was imported into the main code.

To run the web application:

```
python3 -m flash run
```

The webpage is very simple and clean. It has 9 * 9 tiles that allows users to input the values for the Sudoku puzzle that they wish to solve. Next, "Solve!" button can be click to solve the puzzble. The webpage redirects the user to the solved puzzle.

The python Sudoku class allows user to create an empty board, new board input values into the board and solve the board. The algorithm used to solve the Sudoku puzzle is backtracking algorithm. This algorithm is a brute force method. It tries every input possible from 0 to 9 for each tile on the Sudoku puzzle until it solves the puzzle. (Reference: https://www.youtube.com/watch?v=G_UYXzGuqvM&ab_channel=Computerphile) This of course takes a very LONG TIME. The efficiency is O(9 * 9 * 9). This is especially so if the input puzzle is missing alot of tiles. One possible way to improve the efficiency of this algorithm is to include memoization. Adding a database to store solved Sudoku puzzle everytime the web application is being used can be explored. The new algorithm can include checking if the unsolved puzzle matches any of the solved puzzle in the database before solving it. I wonder if it will be more efficient than using the brute force method.

Some feature/improvement to add in the future:
1) Invalid input by user checker
2) Improve backtracking algorithm by including memoization
3) Include sudoku puzzle generator
4) Check for unsolvable Sudoku
5) Link to go back to the main page

