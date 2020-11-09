# SUDOKO SOLVER VISUALIZER

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) </br>
![Python package](https://github.com/99002591/Python-MiniProject/workflows/Python%20package/badge.svg) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/ed646bf27f4148888c90a2cca9d9e0e0)](https://www.codacy.com?utm_source=github.com&utm_medium=referral&utm_content=99002591/Python-MiniProject&utm_campaign=Badge_Grade)

## Collaborators

    > - Amit Das
    > - Smita Senapati
    > - Aditi Dutta

### DESCRIPTION

This is our take on the classic Sudoko puzzle of the size 9x9. </br>
We make use of "Backtracking algorithm" and Pygame to visualize </br>
the steps taken by the algorithm to solve the puzzle, in real time. </br>

### Functionality

    > - The Algorithm
    >   The alogrithm to solve a Sudoko is in the {Algorithm} directory, where main.py calls
    >   solver.py upon execution. It doesn't have a GUI and only prints the result to
    >   the console/terminal.
    > - Visualization of the algorithm
    >   The program GUI.py in the {Implementation} directory, leverages the pygame library to
    >   show, in real time, the steps being taken by the algorithm to solve the Sudoko

### Scope of Improvement 

    > - Addition of a checking mechanism to see if a puzzle is solvable before actually solving it.
    > - Addition of a checking mechanism to check for invalid entries in a given puzzle like repetition of numbers.
    > - Addition of functionily to manually play the puzzle.
