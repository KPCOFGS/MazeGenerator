# MazeGenerator


This generates a maze based on input row and column size. Minimum size is 5x5

## Installation

**Using git**

```bash
git clone https://github.com/KPCOFGS/MazeSolver.git
cd MazeSolver
```

**Install libraries**

```bash
pip install -r requirements.txt
```

## Usage

```bash
python MazeSolver.py
```

## Explanation

The green dot is the starting point and the red dot is the solution

## License

This repository is licensed under the [Unlicense](LICENSE)
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
