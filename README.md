# MazeGenerator
This generates a maze based on input row and column size. Minimum size is 5x5. Do Generate.
Needs to have PIL installed
Fast Use:
import MazeGenerate
row = 101  # values must be odd numbers
column = 55   # values must be odd numbers
maze = MazeGenerate()
maze.generate(row,column)
maze.visualize()
