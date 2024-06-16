from PIL import Image, ImageDraw
import random
import argparse
import os
class Stack():
    def __init__(self):
        self.stack = []
    def push(self,num):
        self.num = num
        self.stack.append(num)
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    def pop(self):
        self.stack.pop(-1)
    def print(self):
        return self.stack
    def last_element(self):
        return self.stack[-1]
    def sort(self,reverse):
        return self.stack.sort(reverse = reverse)
    def extend(self,li):
        self.li = li
        return self.stack.extend(li)
class MazeGenerate():
    def __init__(self):
        pass
    def generate(self,row,column):
        self.row = row
        self.column = column
        maze_shape = []
        action = []
        counter = 0
        maze_shape1 = []
        temp_list = []
        temperory_element = []
        if row % 2 != 1 or row <=4:
            raise TypeError("row size is not proper")
        elif column % 2 != 1 or column <= 4:
            raise TypeError("row size is not proper")
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
                        maze_shape[i][j].append("x")
            else:
                for j in range(column):
                    if j % 2 == 0:
                        maze_shape[i][j].append(i)
                        maze_shape[i][j].append(j)
                        maze_shape[i][j].append("x")
                    else:
                        maze_shape[i][j].append(i)
                        maze_shape[i][j].append(j)
                        maze_shape[i][j].append("u")
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
    def visualizer(self):
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
    def visualize(self,maze,step):
        self.step = step
        self.maze = maze
        rows = len(maze)
        cols = len(maze[0])
        maze_text=[]
        maze_1D = []
        maze_line = ""
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                maze_1D.append(maze[i][j])
            maze_text.append(maze_1D)
            maze_1D = []
        for i in range(len(step)):
            maze_text[step[i][1]][step[i][2]] = "*"
        for i in range(len(maze_text)):
            for j in range(len(maze_text[i])):
                maze_line = maze_line + maze_text[i][j]
            maze_line = maze_line + "\n"
        with open("maze_map.txt","w") as file:
                pass
        for line in maze_line.splitlines():
            with open("maze_map.txt","a") as file:
                file.write(line)
                file.write("\n")
        colors = {
            'x': (0, 0, 0),    # Black
            'a': (0, 255, 0),  # Green
            'b': (255, 0, 0),  # Red
            ' ': (255, 255, 255),  # White
            '*': (255, 255, 0),    # Yellow
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

        # Save the image
        image.save('output_image.png')
generate = MazeGenerate()
parser = argparse.ArgumentParser(description='Input length and height.')
parser.add_argument('--length', dest='length', type=int, required=True, help='Length of the shape')
parser.add_argument('--height', dest='height', type=int, required=True, help='Height of the shape')
parser.add_argument('--action', dest='action', choices=['generate', 'solve'], default='generate', help='Specify whether to generate or solve')

args = parser.parse_args()
action = args.action
row = args.length
column = args.height
generate.generate(row,column)
if action == "generate":
    generate.visualizer()
elif action == "solve":
    stack = Stack()
    solution_not_found = 0
    maze = []
    with open("maze_map.txt",'r') as file:
        maze = file.read().splitlines()
    parent = (0,0,0)
    end = (0,0,0)
    maze_labeled = []
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            maze_labeled.append([maze[row][col],(row,col)])
            if maze[row][col] == 'a':
                parent = [0,row,col,0]
            if maze[row][col] == 'b':
                end = [0,row,col,0]
    action = []
    explored_set = set()
    step_count = 0
    place_holder = []
    while True:
        step_count += 1
        if parent[1] - 1 > -1 and maze[parent[1] - 1][parent[2]] == 'b':
            print(f"solution is found")
            break
        elif parent[1] - 1 > -1 and maze[parent[1] - 1][parent[2]] == ' ' and (parent[1] - 1,parent[2]) not in explored_set:
            block_num = abs((parent[1] - 1) - end[1]) + abs(parent[2] - end[2])
            stack.push([block_num,parent[1] - 1,parent[2],step_count])
        if parent[1] + 1 < len(maze) and maze[parent[1] + 1][parent[2]] == "b":
            print(f"solution is found")
            break
        elif parent[1] + 1 < len(maze) and maze[parent[1] + 1][parent[2]] == ' ' and (parent[1] + 1,parent[2]) not in explored_set:
            block_num = abs((parent[1] + 1) - end[1]) + abs(parent[2] - end[2])
            stack.push([block_num,parent[1] + 1,parent[2],step_count])

        if parent[2]  - 1 > -1 and maze[parent[1]][parent[2]  - 1] == "b":
            print(f"solution is found")
            break
        elif parent[2]  - 1 > -1 and maze[parent[1]][parent[2]  - 1] == ' ' and (parent[1],parent[2] - 1) not in explored_set:
            block_num = abs(parent[1] - end[1]) + abs((parent[2] - 1) - end[2])
            stack.push([block_num,parent[1],parent[2] - 1,step_count])
        if parent[2] + 1 < len(maze[0]) and maze[parent[1]][parent[2] + 1] == "b":
            print(f"solution is found")
            break
        elif parent[2] + 1 < len(maze[0]) and maze[parent[1]][parent[2] + 1] == ' ' and (parent[1],parent[2] + 1) not in explored_set:
            block_num = abs(parent[1] - end[1]) + abs((parent[2] + 1) - end[2])
            stack.push([block_num,parent[1],parent[2] + 1,step_count])
        for i in range(len(stack.print())):
            stack.print()[i][0] = stack.print()[i][0] + stack.print()[i][-1]
        stack.sort(reverse = True)
        try:
            action.append(stack.last_element())
        except:
            solution_not_found = 1
            print("solution not found")
            break
        if len(stack.print()) > 1:
            place_holder.append(action[-1])
        explored_set.add((stack.last_element()[1],stack.last_element()[2]))
        parent = stack.last_element()
        step_count = stack.last_element()[-1]
        stack.pop()

        for i in range(len(stack.print())):
            stack.print()[i][0] = stack.print()[i][0] -  stack.print()[i][-1]

        if maze[parent[1]][parent[2]] == 'b':
            break
    x = []
    y = []
    for i in range(len(action)):
        x.append(action[i][1])
        y.append(action[i][2])
    final_result = []
    try:
        final_result.append(action[-1])
        action.pop()
    except:
        action = []

    score = 0
    length = len(action)
    i = 0
    while action:
        score = 0
        if final_result[i][1] - 1 == action[-1][1] and final_result[i][2] == action[-1][2]:
            score += 1
        if final_result[i][1] + 1 == action[-1][1] and final_result[i][2] == action[-1][2]:
            score += 1
        if final_result[i][2] - 1 == action[-1][2] and final_result[i][1] == action[-1][1]:
            score += 1
        if final_result[i][2] + 1 == action[-1][2] and final_result[i][1] == action[-1][1]:
            score += 1
        if score == 1:
            final_result.append(action[-1])
            action.pop()
        elif score > 1:
            final_result.append(place_holder[-1])
            place_holder.pop()
            for i in range(score):
                action.pop()
        elif score == 0:
            action.pop()
            i = i - 1
        i = i + 1
    final_result.reverse()
    if solution_not_found == 1:
        final_result = []
    generate.visualize(maze,final_result)
try:
    os.remove("maze_map.txt")
except:
    pass