# MazeGenerator
This generates a maze based on input row and column size. Minimum size is 5x5. To Generate, you need to have PIL installed
<br>
Fast Use:
<br>
import MazeGenerate
<br>
row = 101  # values must be odd numbers
<br>
column = 55   # values must be odd numbers
<br>
maze = MazeGenerate.MazeGenerate()
<br>
maze.generate(row,column)
<br>
maze.visualize()
