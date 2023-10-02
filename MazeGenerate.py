import random
from PIL import Image, ImageDraw
class MazeGenerate():
    def __init__(self):
        pass
    def generate(self,row,column):
        # This function uses randomized Depth First Search algorithm to create the maze
        self.row = row
        self.column = column
        maze_shape = []
        action = []
        counter = 0
        maze_shape1 = []
        temp_list = []
        temperory_element = []
        # check if row and column sizes are more than 5 and they are odd numbers
        if row % 2 != 1 or row <=4:
            print("row size is not proper")
            return None
        elif column % 2 != 1 or column <= 4:
            print("column size is not proper")
            return None
        # beginning to create the maze
        for i in range(row):
                for j in range(column):
                    maze_shape1.append([])
                maze_shape.append(maze_shape1)
                maze_shape1 = []
        for i in range(row):
            if i % 2 == 0:
                for j in range(column):
                        maze_shape[i][j].append(i)
                        maze_shape[i][j].append(j)
                        maze_shape[i][j].append("x") # "x" is the wall
            else:
                for j in range(column):
                    if j % 2 == 0:
                        maze_shape[i][j].append(i)
                        maze_shape[i][j].append(j)
                        maze_shape[i][j].append("x")
                    else:
                        maze_shape[i][j].append(i)
                        maze_shape[i][j].append(j)
                        maze_shape[i][j].append("u") # "u" is the undiscovered cell
        # 4 corners, one will be the starting point and another will be the ending point
        vertices = [[maze_shape[1][1]],[maze_shape[-2][1]],[maze_shape[1][-2]],[maze_shape[-2][-2]]]
        current = random.choice(vertices)
        t = current
        current = current[0]
        current[2] = "a"
        vertices.remove(t)
        checkpoint = []
        while True:
            counter = 0
            if current[0] + 2 < row and maze_shape[current[0]+2][current[1]][2] == "u":
                action.append(maze_shape[current[0]+2][current[1]])
                counter = counter + 1
            if current[0] - 2 >= 0 and maze_shape[current[0]-2][current[1]][2] == "u":
                action.append(maze_shape[current[0]-2][current[1]])
                counter = counter + 1
            if current[1] + 2 <column and maze_shape[current[0]][current[1]+2][2] == "u":
                action.append(maze_shape[current[0]][current[1]+2])
                counter = counter + 1
            if current[1] - 2 >=0 and maze_shape[current[0]][current[1]-2][2] == "u":
                action.append(maze_shape[current[0]][current[1]-2])
                counter = counter + 1
            if counter == 0:
                try:
                    current = checkpoint[-1]
                except:
                    break
                checkpoint.pop(-1)
                continue
            if counter > 1:
                checkpoint.append(current)
            if counter > 1:
                for i in range(1,counter+1):
                    temp_list.append(i)
                g = random.sample(temp_list,counter)
                for i in range(counter):
                    temperory_element.append(action[-g[i]])
                for i in range(1,counter+1):
                    action.pop(-1)
                for i in range(counter):
                    action.append(temperory_element[i])               
            temp_list = []
            temperory_element = []
            # if no more actions to take, that means no more "u" cells, so the whole maze is complete
            try:
                action[-1]
            except:
                break
            if current[0] - action[-1][0] == 2:
                maze_shape[current[0]-1][current[1]][2] = " "
            elif current[0] - action[-1][0] == -2:
                maze_shape[current[0]+1][current[1]][2] = " "
            elif current[1] - action[-1][1] == 2:
                maze_shape[current[0]][current[1]-1][2] = " "
            elif current[1] - action[-1][1] == -2:
                maze_shape[current[0]][current[1]+1][2] = " "
            current = action[-1]
            # change u to " "
            current[2] = " "
            #and the path to u change to " "
            action.pop(-1)
        end = random.choice(vertices)
        end[0][2] = "b"
        with open("maze_map.txt","w") as file:
            for i in range(row):
                for j in range(column):
                    file.write(maze_shape[i][j][2])
                file.write("\n")
    def visualize_maze(self):
        colors = {
            'x': (0, 0, 0),    # Black
            'a': (0, 255, 0),  # Green
            'b': (255, 0, 0),  # Red
            ' ': (255, 255, 255),  # White
        }

        # Read the text file
        with open('maze_map.txt', 'r') as file:
            lines = file.readlines()

        # Calculate image dimensions based on the content of the text file
        width = max(len(line.strip()) for line in lines)
        height = len(lines)

        # Create a new image with a white background
        image = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        # Draw each character with the specified color
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                if char in colors:
                    draw.point((x, y), colors[char])

        # Save the image (Optional)
        image.save('output_image.png')

        # Display the image
        image.show()

