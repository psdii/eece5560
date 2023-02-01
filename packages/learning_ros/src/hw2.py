#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist
import sys
import turtle


def move_turtle():

	rospy.init_node('move_turtle', anonymous=True)
	pub = rospy.Publisher('/turtlesim/turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(0.5) 
	
	vel = Twist()
	
	#while not rospy.is_shutdown():
		
	vel.linear.x = 1.0
	vel.linear.y = 0
	
	pub.publish(vel)
	
	rate.sleep()
	
	vel.linear.x = 0
	vel.linear.y = -1.0
	
	pub.publish(vel)
	
	rate.sleep()
	
	vel.linear.x = -1.0
	vel.linear.y = 0
	
	pub.publish(vel)
	
	rate.sleep()
	
	vel.linear.x = 0
	vel.linear.y = 1.0
	
	pub.publish(vel)
	
	rate.sleep()
	
	vel.linear.x = 1.0
	vel.linear.y = 0
	
	pub.publish(vel)
	
	rate.sleep()

if __name__ == '__main__':
	try:
		move_turtle()
	except rospy.ROSInterruptException:
		pass
