from diagonal_movement import DiagonalMovement
from grid import Grid
from a_star import AStarFinder

from util import *

linesFromFile = []

with open("map1.txt") as f:
    for line in f:
        line = line.replace("(", "")
        line = line.replace(")", "")
        line = line.replace("\n", "")
        linesFromFile.append(line)

    matrixCornerFullString = linesFromFile[0]
    matrixCornersArr = matrixCornerFullString.split(' ')

    obstacleList = []

    x = 2
    while linesFromFile[x] != '---':
        print(linesFromFile[x])
        obstacleStrings = linesFromFile[x].split(' ')

        polygon = []

        for string in obstacleStrings:
            polygon.append(string.split(','))
        obstacleList.append(polygon)

        x = x + 1

    x = x + 1

    startList = []
    goalList = []

    while x < len(linesFromFile):
        startAndGoal = linesFromFile[x].split(' ')
        startList.append(startAndGoal[0].split(','))
        goalList.append(startAndGoal[1].split(','))

        x = x + 1

a = matrixCornersArr[0].split(',')

b = matrixCornersArr[1].split(',')

c = matrixCornersArr[2].split(',')

d = matrixCornersArr[3].split(',')

offset_x = 0 - int(d[0])
offset_y = 0 - int(c[1])

for obstacle in obstacleList:
    for point in obstacle:
        point[0] = int(point[0]) + offset_x
        point[1] = int(point[1]) + offset_y

for start in startList:
    start[0] = int(start[0]) + offset_x
    start[1] = int(start[1]) + offset_y

for goal in goalList:
    goal[0] = int(goal[0]) + offset_x
    goal[1] = int(goal[1]) + offset_y

matrixHeight = abs(int(a[1]) - int(b[1]))
matrixWidth = abs(int(a[0]) - int(d[0]))

matrix = []

for row in range(0, matrixHeight * 2):
    rowArr = []
    for col in range(0, matrixWidth * 2):
        rowArr.append(1)
    matrix.append(rowArr)

for y in range(0, matrixHeight * 2):
    for x in range(0, matrixWidth * 2):
        if y + 1 >= matrixHeight * 2 or x + 1 >= matrixWidth * 2:
            continue

        topLeft = matrix[y][x]
        topRight = matrix[y][x + 1]
        botLeft = matrix[y + 1][x]
        botRight = matrix[y + 1][x + 1]

        # topleft

        '''for obstacle in obstacleList:
            if inside_polygon(y, x, obstacle) or on_polygon(y, x, obstacle):
                matrix[y][x] = 0

        # topright
        for obstacle in obstacleList:
            if inside_polygon(y, x + 1, obstacle) or on_polygon(y, x + 1, obstacle):
                matrix[y][x] = 0

        # bottomleft
        for obstacle in obstacleList:
            if inside_polygon(y + 1, x, obstacle) or on_polygon(y + 1, x, obstacle):
                matrix[y][x] = 0

        # bottomright
        for obstacle in obstacleList:
            if inside_polygon(y + 1, x + 1, obstacle) or on_polygon(y + 1, x + 1, obstacle):
                matrix[y][x] = 0
        '''


        obstacle = obstacleList[0]
        #print(obstacle)


        if inside_polygon(x, y ,obstacle) or on_polygon(x, y , obstacle):
            matrix[x][y] = 0
        elif inside_polygon(x+1, y, obstacle) or on_polygon(x+1, y, obstacle):
            matrix[x][y] = 0
        elif inside_polygon(x , y+1, obstacle) or on_polygon(x, y+1, obstacle):
            matrix[x][y] = 0
        elif inside_polygon(x + 1, y + 1, obstacle) or on_polygon(x + 1, y + 1, obstacle):
            matrix[x][y] = 0


        


# print(inside_polygon(3,8,obstacleList[0]))


'''matrix =[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]'''
grid = Grid(matrix=matrix)

start = grid.node(int(startList[0][0]), int(startList[0][1]))
end = grid.node(int(goalList[0][0]), int(goalList[0][1]))

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))
print(path)

for m in range(0, matrixHeight * 2):
    print(matrix[m])







