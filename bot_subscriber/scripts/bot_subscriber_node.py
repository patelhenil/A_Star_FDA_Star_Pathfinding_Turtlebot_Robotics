#! /usr/bin/env python

import rospy
from turtlebot_ctrl.msg import TurtleBotState

def callback(msg):
	x = msg.x
	y = msg.y
	goal_reached = msg.goal_reached
	rospy.loginfo('x: {}, y: {}, goal_reached: {}'.format(x,y,goal_reached))
	



def main():
	rospy.init_node('bot_subscriber_node')
	rospy.Subscriber("/turtlebot_state",TurtleBotState,callback)
	rospy.spin()
	

if __name__ == '__main__':
	main()
