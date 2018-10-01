#! /usr/bin/env python

import sys
import rospy
from turtlebot_ctrl.srv import TurtleBotControl
from geometry_msgs.msg import Point
#TurtleBotControl

from diagonal_movement import DiagonalMovement
from grid import Grid
from a_star import AStarFinder
from fda_star import FDAStarFinder
from turtlebot_ctrl.msg import TurtleBotState

from util import *





def main(choice):
	linesFromFile = []

	with open("/home/duy/catkin_ws/src/comprobfall2018-hw1/turtlebot_maps/map_1.txt") as f:
		for line in f:
			line = line.replace("(", "")
			line = line.replace(")", "")
			line = line.replace("\n", "")
			linesFromFile.append(line)


	print(linesFromFile)

	matrixCornerFullString = linesFromFile[0]
	matrixCornersArr = matrixCornerFullString.split(' ')

    	obstacleList = []

    	x = 2

    	while linesFromFile[x] != '---':

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

	offset_x = 0 - float(d[0])
	offset_y = 0 - float(b[1])

	for obstacle in obstacleList:
	    for point in obstacle:
		point[0] = float(point[0]) + offset_x
		point[1] = float(point[1]) + offset_y

		point[0] = point[0] * 2
		point[1] = point[1] * 2

		temp = point[0]
		point[0] = point[1]
		point[1] = temp

	for start in startList:
	    start[0] = float(start[0]) + offset_x
	    start[1] = float(start[1]) + offset_y
	    start[0] = start[0] * 2
	    start[1] = start[1] * 2

	for goal in goalList:
	    goal[0] = float(goal[0]) + offset_x
	    goal[1] = float(goal[1]) + offset_y
	    goal[0] = goal[0] * 2
	    goal[1] = goal[1] * 2

	matrixHeight = abs(float(a[1]) - float(b[1]))
	matrixWidth = abs(float(a[0]) - float(d[0]))

	matrix = []

	for row in range(0, int(matrixHeight) * 2):
	    rowArr = []
	    for col in range(0, int(matrixWidth) * 2):
		rowArr.append(1)
	    matrix.append(rowArr)

	for x in range(0,int(matrixHeight) * 2):
	    matrix[x][0] = 0
	    matrix[int(matrixHeight) * 2-1][x] = 0
	    matrix[x][int(matrixHeight) * 2-1] = 0
	    matrix[0][x] = 0

	for y in range(0, int(matrixHeight) * 2):
	    for x in range(0, int(matrixWidth) * 2):
		if y + 1 >= matrixHeight * 2 or x + 1 >= matrixWidth * 2:
		    continue


		# topleft

		for obstacle in obstacleList:
		    if inside_polygon(x, y, obstacle) or on_polygon(x, y, obstacle):
		        matrix[x][y] = 0

		# topright
		for obstacle in obstacleList:
		    if inside_polygon(x + 1, y, obstacle) or on_polygon(x + 1, y, obstacle):
		        matrix[x][y] = 0

		# bottomleft
		for obstacle in obstacleList:
		    if inside_polygon(x, y + 1, obstacle) or on_polygon(x, y + 1, obstacle):
		        matrix[x][y] = 0

		# bottomright
		for obstacle in obstacleList:
		    if inside_polygon(x + 1, y + 1, obstacle) or on_polygon(x + 1, y + 1, obstacle):
		        matrix[x][y] = 0

	 
	grid = Grid(matrix=matrix)


	x=6
	start = grid.node(int(startList[x][0]), int(startList[x][1]))
	end = grid.node(int(goalList[x][0]), int(goalList[x][1]))


	if choice == "astar":
    		finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
	else:
    		finder = FDAStarFinder(diagonal_movement=DiagonalMovement.always)
	
	path, runs = finder.find_path(start, end, grid)

	print('operations:', runs, 'path length:', len(path))
	print(grid.grid_str(path=path, start=start, end=end))
	print(path)

	geometryMsgs = rospy.ServiceProxy('/turtlebot_control',TurtleBotControl)

	
	for coor in path:
		x = float(coor[0])/2 - offset_x
		y = float(coor[1])/2 - offset_y

		print("moving to {},{}",x,y)

		point = Point()
		point.x = x
		point.y = y
		point.z = 0

		respond = geometryMsgs(point)

		print("moved to {},{}",x,y)
		print(respond.success)
		print("-------")

if __name__ == '__main__':
	choice = "astar"
	if len(sys.argv) == 2:
    		if sys.argv[1] == "fdastar":
        		choice = "fdastar"


	main(choice)
	
