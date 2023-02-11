#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from math import pow, sqrt
from turtlesim_helper.msg import UnitsLabelled
xprime = 5.55
yprime = 5.55
distravel = 0
def callback(data):
	pub = rospy.Publisher('distance', UnitsLabelled, queue_size=10)
	distance = UnitsLabelled()
	global xprime, yprime, distravel
	dis = sqrt(pow((data.x-xprime),2)+pow((data.y-yprime),2))
	distravel = distravel + dis
	xprime = data.x
	yprime = data.y
	distance.value = distravel
	distance.units = 'meters'
	pub.publish(distance)
	
def distance():
	rospy.init_node('distance',anonymous = True)
	rospy.Subscriber('turtlesim/turtle1/pose', Pose, callback)
	rospy.spin()
	
if __name__ == '__main__':
	distance()
