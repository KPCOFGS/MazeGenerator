# MazeGenerator

This script generates a maze based on the length and height. It will also generate and solve the map if desired. Minimum size is 5x5

## Installation

**Using git**

```bash
git clone https://github.com/KPCOFGS/MazeGenerator.git
cd MazeGenerator
pip install -r requirements.txt
```

## Parameters

`--length LENGTH` Required. Length of the desired map

`--height HEIGHT` Required. Height of the desired map

`--action ACTION` Optional. Either `generate` or `solve`. Default to `generate`

## Usage

```bash
python script.py --length LENGTH --height HEIGHT
```

## Note

* Input values must be an odd number
* The green dot is the starting point and the red dot is the ending point
* If `--action` is set to `solve`, it will generate 2 same maps. One is unsolved and another is solved

## License

This repository is licensed under the [Unlicense](LICENSE)
